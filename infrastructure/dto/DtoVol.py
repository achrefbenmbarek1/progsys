import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proto.donneDesVols.donneDesVols_pb2 import Vol
from .Dto import Dto

class DtoVol(Dto):
    def __init__(self, destination="", nombreDePlaceDispo=-1, prix=-1.0, referance=""):
        self.vol = Vol()
        self.vol.referance = referance
        self.vol.nombreDePlaceDispo = nombreDePlaceDispo
        self.vol.destination = destination
        self.vol.prix = prix

    def serialize(self) -> bytes:
        return self.vol.SerializeToString()

    @staticmethod
    def deserialize(data: bytes) -> 'DtoVol':
        vol = Vol()
        vol.ParseFromString(data)
        return DtoVol(vol.destination, vol.nombreDePlaceDispo, vol.prix, vol.referance)

    def showData(self):
        print(f'Received data: {self.getNombreDePlaceDispo, self.getPrix, self.getReferance}')
        return

    @property
    def getReferance(self) -> str:
        return self.vol.referance

    @property
    def getDestination(self) -> str:
        return self.vol.destination

    @property
    def getNombreDePlaceDispo(self) -> int:
        return self.vol.nombreDePlaceDispo

    @property
    def getPrix(self) -> float:
        return self.vol.prix
