import socket
import os
import sys
import threading
from .Server import Server

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoReferance import DtoReferance
from storage.repository.VolRepository import VolRepository

class ServerUdp(Server):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        print(f'Server listening on {self.host}:{self.port}...')

        while True:
            data,addr = self.sock.recvfrom(4096)
            t = threading.Thread(target=self.handleRequest, args=(data, addr))
            t.start()

    def stop(self):
        self.sock.close()

    def handleRequest(self, data, addr):
        msg = DtoReferance.deserialize(data)
        msg.showData()
        repository = VolRepository("vols.txt")
        dto = repository.readVolByReferance(msg.getReferance)
        self.sock.sendto(dto.serialize(),addr)

