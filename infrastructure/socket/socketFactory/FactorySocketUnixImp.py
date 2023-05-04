import os
import sys
from .FactorySocket import Client, FactorySocket, Server


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from server.ServerUnix import ServerUnix
from client.ClientUnix import ClientUnix
from dto.Dto import Dto

class FactorySocketUnixImp(FactorySocket):
    def __init__(self, sock_path:str,msg:Dto):
        self.sock_path = sock_path
        self.msg = msg

    def getServer(self)->Server:
        server = ServerUnix(self.sock_path)
        return server

    def getClient(self)->Client:
        client = ClientUnix(self.sock_path, self.msg)
        return client
