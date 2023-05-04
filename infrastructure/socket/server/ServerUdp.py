import socket
import os
import sys
from threading import Thread
from .Server import Server

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoReferance import DtoReferance
from storage.repository.RepositoryFactory import RepositoryFactory

class ServerUdp(Server):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        print(f'Server listening on {self.host}:{self.port}...')

        while True:
            data, addr = self.sock.recvfrom(1024)
            print(f'Connected by {addr}')
            t = Thread(target=self.handleRequest, args=(data, addr))
            t.start()

    def handleRequest(self, data, addr):
        msg = DtoReferance.deserialize(data)
        print(f'type of data: {type(msg)}')
        msg.showData()
        repositoryFactory = RepositoryFactory(msg.getDataType)
        repository = repositoryFactory.createRepository()
        if msg.getDataType == "vol":
            dto = repository.readVolByReferance(msg.getReferance)
            self.sock.sendto(dto.serialize(), addr)
        elif msg.getDataType == "facture":
            dto = repository.readFactureByReferance(msg.getReferance)
            self.sock.sendto(dto.serialize(), addr)
        elif msg.getDataType == "transactionHistory" and msg.getMethod == "get":
            dto = repository.readHistory()
            self.sock.sendto(dto.serialize(), addr)

    def stop(self):
        self.sock.close()

