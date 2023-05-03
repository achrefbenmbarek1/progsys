from abc import ABC, abstractmethod

from ..client.Client import Client
from ..server.Server import Server


class FactorySocket(ABC):
    @abstractmethod
    def getServer(self, protocol:str)->Server:
        pass

    @abstractmethod
    def getClient(self, protocol:str)->Client:
        pass
