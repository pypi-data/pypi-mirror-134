"""Concrete ModbusPDU implementations for GivEnergy-specific requests and responses."""

from __future__ import annotations

import logging
from abc import ABC
from typing import Any, Callable

from crccheck.crc import CrcModbus
from pymodbus import pdu as pymodbus_pdu
from pymodbus.constants import Endian
from pymodbus.interfaces import IModbusSlaveContext
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder

from .util import friendly_class_name, hexxed

_logger = logging.getLogger(__package__)


class ModbusPDU(ABC):
    """Base of the PDU handler tree. Defines the most common shared attributes and code."""

    builder: BinaryPayloadBuilder
    function_code: int
    data_adapter_serial_number: str = 'AB1234G567'
    padding: int = 0x00000008
    slave_address: int = 0x32
    check: int = 0x0000

    def __init__(self, **kwargs):
        """Constructor."""
        if "function_id" in kwargs:  # TODO can be removed?
            raise ValueError("function_id= is not valid, use function_code= instead.", self)

        if "function_code" in kwargs:  # TODO can be removed?
            if not hasattr(self, 'function_code') or kwargs["function_code"] != self.function_code:
                raise ValueError(
                    f"Specified function code {kwargs['function_code']} is different "
                    f"from what {self} is expecting.",
                    self,
                )
            del kwargs['function_code']
        kwargs.update(  # ensure these can never get overwritten  TODO can be removed?
            {
                "transaction": 0x5959,
                "protocol": 0x0001,
                "unit": 0x01,
                "skip_encode": True,
            }
        )
        super().__init__(**kwargs)
        self._set_attribute_if_present('data_adapter_serial_number', kwargs)
        self._set_attribute_if_present('padding', kwargs)
        self._set_attribute_if_present('slave_address', kwargs)
        self._set_attribute_if_present('check', kwargs)

    def __str__(self):
        """Returns a useful string representation of the PDU and its internal state."""
        if hasattr(self, 'function_code'):
            fn_code = self.function_code
        else:
            fn_code = '_'
        filtered_keys = ['transaction_id', 'protocol_id', 'unit_id', 'skip_encode']  # these mean nothing
        filtered_vars = ', '.join([f'{k}: {hexxed(v)}' for k, v in vars(self).items() if k not in filtered_keys])
        if len(filtered_vars) > 0:
            filtered_vars = '{' + filtered_vars + '}'
        return f"{fn_code}/{friendly_class_name(self.__class__)}({filtered_vars})"

    def _set_attribute_if_present(self, attr: str, kwargs: dict[str, Any]):
        if attr in kwargs:
            setattr(self, attr, kwargs[attr])

    def encode(self) -> bytes:
        """Encode PDU message from instance attributes."""
        self._ensure_valid_state()
        self.builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        self.builder.add_string(f"{self.data_adapter_serial_number[-10:]:*>10}")  # ensure exactly 10 bytes
        self.builder.add_64bit_uint(self.padding)
        self.builder.add_8bit_uint(self.slave_address)
        self.builder.add_8bit_uint(self.function_code)
        self._encode_function_data()
        self._update_check_code()
        return self.builder.to_string()

    def decode(self, data: bytes) -> None:
        """Decode PDU message and populate instance attributes."""
        decoder = BinaryPayloadDecoder(data, byteorder=Endian.Big)
        self.data_adapter_serial_number = decoder.decode_string(10).decode("ascii")
        self.padding = decoder.decode_64bit_uint()
        self.slave_address = decoder.decode_8bit_uint()
        function_code = decoder.decode_8bit_uint()
        if self.function_code != function_code:
            e = ValueError(
                f"Expected function code 0x{self.function_code:02x}, found 0x{function_code:02x} instead.", self
            )
            _logger.exception(e)
            raise e

        self._decode_function_data(decoder)
        self._ensure_valid_state()
        _logger.debug(f"Successfully decoded {len(data)} bytes")

    def _encode_function_data(self) -> None:
        """Complete function-specific encoding of the remainder of the PDU message."""
        raise NotImplementedError()

    def _decode_function_data(self, decoder: BinaryPayloadDecoder) -> None:
        """Complete function-specific decoding of the remainder of the PDU message."""
        raise NotImplementedError()

    def _update_check_code(self) -> None:
        """Recalculate CRC of the PDU message."""
        raise NotImplementedError()

    def _ensure_valid_state(self) -> None:
        """Sanity check our internal state."""
        raise NotImplementedError()

    def get_response_pdu_size(self) -> int:
        """Allows the framer to decapsulate the PDU properly from the MBAP frame header."""
        # 20 = 10 (data adapter serial) + 8 (padding) + 1 (slave addr) + 1 (function code)
        size = 20 + self._calculate_function_data_size()
        _logger.debug(f"Calculated {size} bytes total response PDU size for {self}")
        if size >= 247:
            _logger.error('Expected response size {size}b exceeds Modbus protocol spec.')
        return size

    def _calculate_function_data_size(self) -> int:
        raise NotImplementedError()

    def execute(self, context) -> ModbusPDU:
        """Called to create the Response PDU after an incoming message has been completely processed."""
        raise NotImplementedError()


#################################################################################
class ModbusRequest(ModbusPDU, pymodbus_pdu.ModbusRequest, ABC):
    """Root of the hierarchy for Request PDUs."""

    def execute(self, context: IModbusSlaveContext) -> ModbusResponse:
        """Hook that allows a Response PDU to be created from the same context where the Request was handled.

        Args:
            context: A datastore context that should be able to provide the values to populate the Response with.
        """
        # if not (1 <= self.register_count <= 0x7D0):
        #     return self.doException(ModbusExceptions.IllegalValue)
        # if not context.validate(self.function_code, self.base_register, self.register_count):
        #     return self.doException(ModbusExceptions.IllegalAddress)
        # values = context.getValues(self.function_code, self.address, self.count)
        # return ReadRegistersResponse(values)  # echo back some values from the Request in the Response
        raise NotImplementedError()


class ModbusResponse(ModbusPDU, pymodbus_pdu.ModbusResponse, ABC):
    """Root of the hierarchy for Response PDUs."""

    def _update_check_code(self):
        # Until we know how Responses are checksummed there's nothing we can do here; self.check stays 0x0000
        _logger.warning('Unable to recalculate checksum, using whatever value was set')
        self.builder.add_16bit_uint(self.check)

    def execute(self, context) -> ModbusPDU:
        """There is no automatic Reply following the processing of a Response."""
        pass


#################################################################################
class ReadRegistersRequest(ModbusRequest, ABC):
    """Handles all messages that request a range of registers."""

    def __init__(self, **kwargs):
        """Constructor."""
        super().__init__(**kwargs)
        self.base_register = kwargs.get('base_register', 0x0000)
        self.register_count = kwargs.get('register_count', 0x0000)

    def _encode_function_data(self):
        self.builder.add_16bit_uint(self.base_register)
        self.builder.add_16bit_uint(self.register_count)

    def _decode_function_data(self, decoder):
        self.base_register = decoder.decode_16bit_uint()
        self.register_count = decoder.decode_16bit_uint()
        self.check = decoder.decode_16bit_uint()

    def _update_check_code(self):
        crc_builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        crc_builder.add_8bit_uint(self.function_code)
        crc_builder.add_16bit_uint(self.base_register)
        crc_builder.add_16bit_uint(self.register_count)
        self.check = CrcModbus().process(crc_builder.to_string()).final()
        self.builder.add_16bit_uint(self.check)

    def _calculate_function_data_size(self):
        size = 16 + (self.register_count * 2)
        _logger.debug(f"Calculated {size} bytes partial response size for {self}")
        return size

    def _ensure_valid_state(self):
        if self.base_register is None:
            raise ValueError('Base Register must be set explicitly.')
        elif not 0 <= self.base_register <= 0xFFFF:
            raise ValueError(f'Base Register {hex(self.base_register)} must be unsigned and fit in 2 bytes')
        if self.register_count is None:
            raise ValueError('Register Count must be set explicitly.')
        elif not 0 <= self.register_count <= 0xFFFF:
            raise ValueError(f'Register Count {hex(self.register_count)} must be unsigned and fit in 2 bytes')

        if self.register_count > 60:
            # should we abort instead?
            _logger.warning('GivEnergy devices do not return more than 60 registers per call, this will likely fail.')


class ReadRegistersResponse(ModbusResponse, ABC):
    """Handles all messages that respond with a range of registers."""

    def __init__(self, **kwargs):
        """Constructor."""
        super().__init__(**kwargs)
        self.inverter_serial_number: str = kwargs.get('inverter_serial_number', 'SA1234G567')
        self.base_register: int = kwargs.get('base_register', 0x0000)
        self.register_count: int = kwargs.get('register_count', 0x0000)
        self.register_values: list[int] = kwargs.get('register_values', [])
        if self.register_count != len(self.register_values):
            raise ValueError(
                f'Expected to receive {self.register_count} register values, '
                f'instead received {len(self.register_values)}.',
                self,
            )
        # self.check: int = kwargs.get('check', 0x0000)

    def _encode_function_data(self):
        self.builder.add_string(f"{self.inverter_serial_number[-10:]:*>10}")  # ensure exactly 10 bytes
        self.builder.add_16bit_uint(self.base_register)
        self.builder.add_16bit_uint(self.register_count)
        [self.builder.add_16bit_uint(v) for v in self.register_values]

    def _decode_function_data(self, decoder):
        """Decode response PDU message and populate instance attributes."""
        self.inverter_serial_number = decoder.decode_string(10).decode("ascii")
        self.base_register = decoder.decode_16bit_uint()
        self.register_count = decoder.decode_16bit_uint()
        self.register_values = [decoder.decode_16bit_uint() for i in range(self.register_count)]
        if self.register_count != len(self.register_values):
            raise ValueError(
                f'Expected to receive {self.register_count} register values, '
                f'instead received {len(self.register_values)}.',
                self,
            )
        self.check = decoder.decode_16bit_uint()

    def _ensure_valid_state(self):
        if self.register_count == 60 and set(self.register_values) == {0}:
            raise AssertionError('Read back 60 zero-valued registers which is suspicious.')

    def to_dict(self):
        """Return the registers as a dict of register_index:value. Accounts for base_register offsets."""
        return {k: v for k, v in enumerate(self.register_values, start=self.base_register)}


#################################################################################
class ReadHoldingRegistersMeta:
    """Request & Response PDUs for function 3/Read Holding Registers."""

    function_code = 3


class ReadHoldingRegistersRequest(ReadHoldingRegistersMeta, ReadRegistersRequest):
    """Concrete PDU implementation for handling 3/Read Holding Registers request messages."""

    def execute(self, context) -> ModbusResponse:
        """FIXME if we ever implement a server."""
        raise NotImplementedError()


class ReadHoldingRegistersResponse(ReadHoldingRegistersMeta, ReadRegistersResponse):
    """Concrete PDU implementation for handling 3/Read Holding Registers request messages."""

    def _calculate_function_data_size(self) -> int:
        raise NotImplementedError()


#################################################################################
class ReadInputRegistersMeta:
    """Request & Response PDUs for function 4/Read Input Registers."""

    function_code = 4


class ReadInputRegistersRequest(ReadInputRegistersMeta, ReadRegistersRequest):
    """Concrete PDU implementation for handling 4/Read Input Registers request messages."""

    def execute(self, context) -> ModbusResponse:
        """FIXME if we ever implement a server."""
        raise NotImplementedError()


class ReadInputRegistersResponse(ReadInputRegistersMeta, ReadRegistersResponse):
    """Concrete PDU implementation for handling 4/Read Input Registers response messages."""

    def _calculate_function_data_size(self) -> int:
        raise NotImplementedError()


#################################################################################
class WriteHoldingRegisterMeta:
    """Request & Response PDUs for function 6/Write Holding Register."""

    function_code = 6


class WriteHoldingRegisterRequest(WriteHoldingRegisterMeta, ModbusRequest, ABC):
    """Handles all messages that request a range of registers."""

    writable_registers = {
        20,  # ENABLE_CHARGE_TARGET
        27,  # BATTERY_POWER_MODE
        31,  # CHARGE_SLOT_2_START
        32,  # CHARGE_SLOT_2_END
        35,  # SYSTEM_TIME_YEAR
        36,  # SYSTEM_TIME_MONTH
        37,  # SYSTEM_TIME_DAY
        38,  # SYSTEM_TIME_HOUR
        39,  # SYSTEM_TIME_MINUTE
        40,  # SYSTEM_TIME_SECOND
        44,  # DISCHARGE_SLOT_2_START
        45,  # DISCHARGE_SLOT_2_END
        56,  # DISCHARGE_SLOT_1_START
        57,  # DISCHARGE_SLOT_1_END
        59,  # ENABLE_DISCHARGE
        94,  # CHARGE_SLOT_1_START
        95,  # CHARGE_SLOT_1_END
        96,  # CHARGE_ENABLE
        110,  # BATTERY_SOC_RESERVE
        111,  # BATTERY_CHARGE_LIMIT
        112,  # BATTERY_DISCHARGE_LIMIT
        114,  # BATTERY_DISCHARGE_MIN_POWER_RESERVE
        116,  # TARGET_SOC
    }

    def __init__(self, **kwargs):
        """Constructor."""
        super().__init__(**kwargs)
        self.register: int = kwargs.get('register', None)
        self.value: int = kwargs.get('value', None)

    def _encode_function_data(self):
        self.builder.add_16bit_uint(self.register)
        self.builder.add_16bit_uint(self.value)

    def _decode_function_data(self, decoder):
        self.register = decoder.decode_16bit_uint()
        self.value = decoder.decode_16bit_uint()
        self.check = decoder.decode_16bit_uint()

    def _update_check_code(self):
        crc_builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        crc_builder.add_8bit_uint(self.function_code)
        crc_builder.add_16bit_uint(self.register)
        crc_builder.add_16bit_uint(self.value)
        self.check = CrcModbus().process(crc_builder.to_string()).final()
        self.builder.add_16bit_uint(self.check)

    def _calculate_function_data_size(self):
        size = 16
        _logger.debug(f"Calculated {size} bytes partial response size for {self}")
        return size

    def _ensure_valid_state(self):
        if self.register not in self.writable_registers:
            raise ValueError(f'Register {self.register} is not safe to write to.')
        if self.value is None:
            raise ValueError('Value must be set explicitly.')
        elif not 0 <= self.value <= 0xFFFF:
            raise ValueError(f'Value {hex(self.value)} must be unsigned and fit in 2 bytes')


class WriteHoldingRegisterResponse(WriteHoldingRegisterMeta, ModbusResponse, ABC):
    """Handles all messages that respond with a range of registers."""

    def __init__(self, **kwargs):
        """Constructor."""
        super().__init__(**kwargs)
        self.inverter_serial_number: str = kwargs.get('inverter_serial_number', 'SA1234G567')
        self.register: int = kwargs.get('register', None)
        self.value: int = kwargs.get('value', None)

    def _encode_function_data(self):
        self.builder.add_string(f"{self.inverter_serial_number[-10:]:*>10}")  # ensure exactly 10 bytes
        self.builder.add_16bit_uint(self.register)
        self.builder.add_16bit_uint(self.value)

    def _decode_function_data(self, decoder):
        """Decode response PDU message and populate instance attributes."""
        self.inverter_serial_number = decoder.decode_string(10).decode("ascii")
        self.register = decoder.decode_16bit_uint()
        self.value = decoder.decode_16bit_uint()
        self.check = decoder.decode_16bit_uint()

    def _ensure_valid_state(self):
        if self.register is None:
            raise ValueError('Register must be set explicitly.')
        if self.value is None:
            raise ValueError('Value must be set explicitly.')


#################################################################################
# Authoritative catalogue of Request/Response PDUs the Decoder factories will consider.
REQUEST_PDUS: list[Callable] = [
    ReadHoldingRegistersRequest,
    ReadInputRegistersRequest,
    WriteHoldingRegisterRequest,
]
RESPONSE_PDUS: list[Callable] = [
    ReadHoldingRegistersResponse,
    ReadInputRegistersResponse,
    WriteHoldingRegisterResponse,
]
