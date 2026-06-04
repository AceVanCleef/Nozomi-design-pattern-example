from abc import ABC, abstractmethod

class ProtocolParser(ABC):
    @abstractmethod    
    def can_parse(self, stream: bytes) -> bool:
        '''Checks whether the byte stream can be parsed.'''
        pass
    
    @abstractmethod
    def parse_message(self, stream: bytes) -> str:
        '''Extracts the message from the byte stream.'''
        pass