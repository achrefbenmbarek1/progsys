import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proto.referance.referance_pb2 import Request
from .Dto import Dto

class DtoReferance(Dto):
    def __init__(self, referance, dataType:str, method:str):
        self.referanceObject = Request()
        self.referanceObject.referance = referance
        self.referanceObject.dataType = dataType
        self.referanceObject.method = method

    def serialize(self) -> bytes:
        return self.referanceObject.SerializeToString()

    @staticmethod
    def deserialize(data: bytes) -> 'DtoReferance':
        referanceObject = Request()
        referanceObject.ParseFromString(data)
        return DtoReferance(referanceObject.referance, referanceObject.dataType, referanceObject.method)

    def showData(self):
        print(f'Received data: {self.getReferance, self.getDataType, self.getMethod}')
        return

    @property
    def getReferance(self) -> str:
        return self.referanceObject.referance

    @property
    def getDataType(self) -> str:
        return self.referanceObject.dataType

    @property
    def getMethod(self) -> str:
        return self.referanceObject.method

