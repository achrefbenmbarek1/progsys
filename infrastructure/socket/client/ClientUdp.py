import socket
import sys
import os

from .Client import Client
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.Dto import Dto
from dto.dtoFactory.DtoFactory import DtoFactory


class ClientUdp(Client):

    def __init__(self, host:str, port:int, msg:Dto):
        self.host = host
        self.port = port
        self.msg = msg

    def send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self.msg.serialize(), (self.host, self.port))
        response, server_address = sock.recvfrom(1024)
        dtoFactory = DtoFactory() 
        dto = dtoFactory.create(self.msg.getDataType,response)
        print(f'Received response: {type(dto)}')
        dto.showData()
        sock.close()

