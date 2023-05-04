import socket
import os
import sys
from threading import Thread
from .Server import Server

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoReferance import DtoReferance
from storage.repository.RepositoryFactory import RepositoryFactory

class ServerTcp(Server):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f'Server listening on {self.host}:{self.port}...')

        while True:
            conn, addr = self.sock.accept()
            print(f'Connected by {addr}')
            t = Thread(target=self.handleRequest, args=(conn,))
            t.start()

    def handleRequest(self,conn ):
            data = conn.recv(1024)
            if not data:
                conn.close()
                return
            msg = DtoReferance.deserialize(data)
            print(f'type of data: {type(msg)}')
            msg.showData()
            repositoryFactory = RepositoryFactory(msg.getDataType)
            repository = repositoryFactory.createRepository()
            if msg.getDataType == "vol":
                dto = repository.readVolByReferance(msg.getReferance)
                conn.send(dto.serialize())
            elif msg.getDataType == "facture":
                dto = repository.readFactureByReferance(msg.getReferance)
                conn.send(dto.serialize())
            elif msg.getDataType == "transactionHistory" and msg.getMethod == "get":
                dto = repository.readHistory()
                conn.send(dto.serialize())
                
            conn.close()

    def stop(self):
        self.sock.close()
