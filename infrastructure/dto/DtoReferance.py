from .Dto import Dto

class DtoReferance(Dto):
    def __init__(self, referance):
        self.referance = referance

    def serialize(self) -> bytes:
        return self.referance.encode()

    @staticmethod
    def deserialize(data: bytes) -> 'DtoReferance':
        return DtoReferance(data.decode())

    def showData(self):
        print(f'Received data: {self.getReferance}')
        return

    @property
    def getReferance(self) -> str:
        return self.referance

