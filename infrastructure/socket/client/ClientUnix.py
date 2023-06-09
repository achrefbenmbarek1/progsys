import socket
import sys
import os

from .Client import Client
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.Dto import Dto
from dto.dtoFactory.DtoFactory import DtoFactory


class ClientUnix(Client):

    def __init__(self, socket_file:str, msg:Dto):
        self.socket_file = socket_file
        self.msg = msg

    def send(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.socket_file)
        sock.sendall(self.msg.serialize())
        response =sock.recv(1024)
        dtoFactory = DtoFactory() 
        dto = dtoFactory.create(self.msg.getDataType,response)
        print(f'Received response: {type(dto)}')
        dto.showData()
        sock.close()
