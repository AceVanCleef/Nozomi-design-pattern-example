from .protocol_parser import ProtocolParser

class GenericTcpUdpParser(ProtocolParser):
    def can_parse(self, stream: bytes) -> bool:
        return True
    
    def parse_message(self, stream: bytes) -> str:
        try:
            message = stream.decode('ascii', errors='strict')
        except UnicodeDecodeError as e:
            print("Decoding Error:", e)
            
        return message