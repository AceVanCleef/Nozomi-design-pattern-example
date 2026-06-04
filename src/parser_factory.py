from typing import List
from src.parser.generic_tcp_udp_parser import GenericTcpUdpParser
from src.parser.modbus_parser import ModbusParser
from src.parser.profibus_parser import ProfibusParser
from src.parser.protocol_parser import ProtocolParser

class ParserFactory:
    @staticmethod
    def get_parser(stream: bytes) -> ProtocolParser:
        parsers: List[ProtocolParser] = [
            ProfibusParser(),
            ModbusParser(),
            GenericTcpUdpParser()
        ]
        
        for p in parsers:
            if  p.can_parse(stream):
                return p