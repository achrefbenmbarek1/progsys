import os
import sys
from .FactorySocket import Client, FactorySocket, Server


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from server.ServerTcp import ServerTcp
from client.ClientTcp import ClientTcp
from dto.Dto import Dto

class FactorySocketTcpImp(FactorySocket):
    def __init__(self, host:str, port:int, dto:Dto):
        self.host = host
        self.port = port
        self.dto = dto

    def getServer(self)->Server:
        server = ServerTcp(self.host, self.port)
        return server

    def getClient(self)->Client:
        client = ClientTcp(self.host, self.port, self.dto)
        return client
