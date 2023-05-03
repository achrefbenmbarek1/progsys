import os
import sys
from .FactorySocket import Client, FactorySocket, Server


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from server.ServerUdp import ServerUdp
from client.ClientUdp import ClientUdp
from dto.Dto import Dto


class FactorySocketUdpImp(FactorySocket):
    def __init__(self, host:str, port:int, dto:Dto):
        self.host = host
        self.port = port
        self.dto = dto

    def getServer(self)->Server:
        server = ServerUdp(self.host, self.port)
        return server

    def getClient(self)->Client:
        # referance = input("saisir la referance du vol")
        # destination = input("saisir la destination du vol")
        # nombreDePlaceDispo = int(input("saisir le nombreDePlaceDispo du vol"))
        # prix = float(input("saisir le prix du vol"))
        # msg = DtoVol(destination, nombreDePlaceDispo, prix, referance)
        # client = ClientUdp(self.host, self.port, msg)
        client = ClientUdp(self.host, self.port, self.dto)
        return client
