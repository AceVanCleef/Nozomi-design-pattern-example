from .protocol_parser import ProtocolParser

class ModbusParser(ProtocolParser):
    def can_parse(self, stream: bytes) -> bool:
        return stream[2] == int(0x00) and stream[3] == int(0x00)
    
    def parse_message(self, stream: bytes) -> str:
        try:
            message_len = stream[7]
            message_payload = stream[8:8 + message_len]
            message = message_payload.decode('ascii', errors='strict')
        except UnicodeDecodeError as e:
            print("Decoding Error:", e)
            
        return message