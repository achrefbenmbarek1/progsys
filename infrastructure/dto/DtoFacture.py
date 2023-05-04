import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proto.donneDesFactures.donneDesFactures_pb2 import Facture
from .Dto import Dto

class DtoFacture(Dto):
    def __init__(self, referance:str="",sommeAPayer:str=""):
        self.facture = Facture()
        self.facture.referance = referance
        self.facture.sommeAPayer = sommeAPayer

    def serialize(self) -> bytes:
        return self.facture.SerializeToString()

    @staticmethod
    def deserialize(data: bytes) -> 'DtoFacture':
        facture = Facture()
        facture.ParseFromString(data)
        return DtoFacture(facture.referance,facture.sommeAPayer)

    def showData(self):
        print(f'Received data: {self.getReferance, self.getSommeAPayer}')
        return

    @property
    def getReferance(self) -> str:
        return self.facture.referance

    @property
    def getSommeAPayer(self) -> str:
        return self.facture.sommeAPayer

