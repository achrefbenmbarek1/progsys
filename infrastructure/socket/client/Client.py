from abc import ABC, abstractmethod

class Client(ABC):
    @abstractmethod
    def send(self):
        pass
