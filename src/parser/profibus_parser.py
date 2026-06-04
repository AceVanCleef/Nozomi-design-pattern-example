from .protocol_parser import ProtocolParser

class ProfibusParser(ProtocolParser):
    def can_parse(self, stream: bytes) -> bool:
        return stream[0] == int(0x68) and stream[3] == int(0x68) and stream[1] == stream[2]
    
    def parse_message(self, stream: bytes) -> str:
        if stream[1] != stream[2]:
            raise ValueError('Invalid Profibus frame: Length bytes do not match.')

        try:
            message_len = stream[1]
            message_payload = stream[4: 5 + message_len - 1]
            message = message_payload.decode('ascii', errors='strict')
        except UnicodeDecodeError as e:
            print("Decoding Error:", e)
            
        return message