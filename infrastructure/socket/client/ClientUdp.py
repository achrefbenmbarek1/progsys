import socket
import sys
import os

# from gestionDesVols.dto.DtoVol import DtoVol
from .Client import Client

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoVol import DtoVol

class ClientUdp(Client):

    def __init__(self, host, port, msg:DtoVol):
        self.host = host
        self.port = port
        self.msg = msg

    def send(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self.msg.serialize(),(self.host, self.port))
        sock.close()
