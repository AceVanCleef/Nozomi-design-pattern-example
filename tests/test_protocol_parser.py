import pytest

from src.parser.generic_tcp_udp_parser import GenericTcpUdpParser
from src.parser.modbus_parser import ModbusParser
from src.parser.profibus_parser import ProfibusParser
from src.parser_factory import ParserFactory

# Arrange
# Note that some bytes have been ommitted to simplify this demo.
profibus_stream = bytes([
    0x68, # initial protocol identifier
    0x0E, 0x0E, # represent length of the message
    0x68, # second protocol identifier
    72, 101, 108, 108, 111, 32, 80, 114, 111, 102, 105, 98, 117, 115, 
    0x16 # end delimiter
])

# Note that some bytes have been ommitted to simplify this demo.
modbus_stream = bytes([
    0x00, 0x01, 
    0x00, 0x00, # identifies the protocol
    0x00, 0x0D, 0x01,
    0xc, # represents the length of the message
    72, 101, 108, 108, 111, 32, 77, 111, 100, 98, 117, 115
])

# A plain ASCII-encoded string payload - without signature.
tcp_udp_stream = bytes([
    72, 101, 108, 108, 111, 32, 71, 101, 110, 101, 114, 105, 103, 32, 84, 67, 
    80, 47, 85, 68, 80
])

@pytest.mark.parametrize(
    "input_stream, expected_message",
    [
        pytest.param(
            profibus_stream,
            "Hello Profibus",
            id="Profibus (Simplified)"
        ),
        pytest.param(
            modbus_stream, 
            "Hello Modbus", 
            id="ModBus TCP (Simplified)"
        ),
        pytest.param(
            tcp_udp_stream,
            "Hello Generig TCP/UDP",
            id="Generic TCP/UDP"
        ),
    ]
)
def test_parse_message(input_stream, expected_message):
    # Arrange
    parser = ParserFactory.get_parser(input_stream)
    
    # Act
    result = parser.parse_message(input_stream)
    
    # Assert
    assert result == expected_message

@pytest.mark.parametrize(
    "input_stream, is_profibus, is_modbus, is_generic_tcp_udp",
    [
        pytest.param(profibus_stream, True, False, True, id="Logic: Can Parse Profibus (Simplified)"),
        pytest.param(modbus_stream, False, True, True, id="Logic: Can Parse Modbus (Simplified)"),
        pytest.param(tcp_udp_stream, False, False, True, id="Logic: Can Parse Generic TCP/UDP"),
    ]
)
def test_can_parse(input_stream, is_profibus, is_modbus, is_generic_tcp_udp):
    # Arrange
    profibus_parser = ProfibusParser()
    modbus_parser = ModbusParser()
    generic_tcp_udp_parser = GenericTcpUdpParser()
    
    # Act
    profibus_result = profibus_parser.can_parse(input_stream)
    modbus_result = modbus_parser.can_parse(input_stream)
    generic_tcp_udp_result = generic_tcp_udp_parser.can_parse(input_stream)
    
    # Assert
    assert profibus_result == is_profibus
    assert modbus_result == is_modbus
    assert generic_tcp_udp_result == is_generic_tcp_udp

@pytest.mark.skip(reason="TBD: Test behaviour for UnicodeDecodeErrors.")
def test_all_parser_decoding_error_handling():
    pass

@pytest.mark.skip(reason="TBD: Test behaviour for corrupted length bytes.")
def test_profibus_parser_error_handling():
    pass