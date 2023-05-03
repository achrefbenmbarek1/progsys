from abc import ABC, abstractmethod

from ..client.Client import Client
from ..server.Server import Server


class FactorySocket(ABC):
    @abstractmethod
    def getServer(self)->Server:
        pass

    @abstractmethod
    def getClient(self)->Client:
        pass
