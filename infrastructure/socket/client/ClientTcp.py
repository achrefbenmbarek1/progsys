import socket
import sys
import os

# from gestionDesVols.dto.DtoVol import DtoVol
from .Client import Client
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoVol import DtoVol
from dto.Dto import Dto

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "..")))

class ClientTcp(Client):

    def __init__(self, host, port, msg:DtoVol):
        self.host = host
        self.port = port
        self.msg = msg

    def send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.sendall(self.msg.serialize())
        response =sock.recv(1024)

# Deserialize the response into a DtoVol object
        response_dto = Dto.deserialize(response)
        print(f'Received response: {type(response_dto)}')
        response_dto.showData()

        sock.close()

