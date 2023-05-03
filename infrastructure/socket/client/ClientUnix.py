import socket
import sys
import os

# from gestionDesVols.dto.DtoVol import DtoVol
from .Client import Client

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoVol import DtoVol

class ClientUnix(Client):

    def __init__(self, sock_path, msg:DtoVol):
        self.sock_path = sock_path
        self.msg = msg

    def send(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.sock_path)
        sock.sendall(self.msg.serialize())
        sock.close()
