import os
import sys
from .FactorySocket import Client, FactorySocket, Server


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from server.ServerTcp import ServerTcp
from client.ClientTcp import ClientTcp
from dto.DtoVol import DtoVol

class FactorySocketTcpImp(FactorySocket):
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port

    def getServer(self)->Server:
        server = ServerTcp(self.host, self.port)
        return server

    def getClient(self)->Client:
        referance = input("saisir la referance du vol")
        destination = input("saisir la destination du vol")
        nombreDePlaceDispo = int(input("saisir le nombreDePlaceDispo du vol"))
        prix = float(input("saisir le prix du vol"))
        msg = DtoVol(destination, nombreDePlaceDispo, prix, referance)
        client = ClientTcp(self.host, self.port, msg)
        return client
