import os
import sys
import socket
from threading import Thread

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoReferance import DtoReferance
from storage.repository.RepositoryFactory import RepositoryFactory

class ServerUnix:
    def __init__(self, socket_file):
        self.socket_file = socket_file

    def start(self):
        try:
            os.unlink(self.socket_file)  
        except OSError:
            pass

        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.bind(self.socket_file)
        self.sock.listen(1)
        print(f'Server listening on {self.socket_file}...')

        while True:
            conn, addr = self.sock.accept()
            print(f'Connected by {addr}')
            t = Thread(target=self.handleRequest, args=(conn,))
            t.start()

    def handleRequest(self, conn):
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
        try:
            os.unlink(self.socket_file)
        except OSError:
            pass


