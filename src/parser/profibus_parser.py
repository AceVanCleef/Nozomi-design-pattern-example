from .protocol_parser import ProtocolParser

class ProfibusParser(ProtocolParser):
    def can_parse(self, stream: bytes) -> bool:
        pass
    
    def parse_message(self, stream: bytes) -> str:
        pass