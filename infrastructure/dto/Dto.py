from abc import ABC, abstractmethod
# from typing import Any

class Dto(ABC):
    @abstractmethod
    def serialize(self) -> bytes:
        pass
    
    # @staticmethod
    # @abstractmethod
    # def deserialize(data: bytes) -> 'Dto':
    #     pass
    @classmethod
    def deserialize(cls, data: bytes) -> 'Dto':
        for subclass in cls.__subclasses__():
            try:
                return subclass.deserialize(data)
            except:
                pass
        raise ValueError('Invalid DTO data')

    @abstractmethod
    def showData(self):
        pass
