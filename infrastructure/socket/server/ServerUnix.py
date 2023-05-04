# import socket
# import os
# import sys
# from .Server import Server
#
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
# from dto.DtoVol import DtoVol
#
# class ServerUnix(Server):
#     def __init__(self, sock_path):
#         self.sock_path = sock_path
#
#     def start(self):
#         try:
#             os.unlink(self.sock_path)
#         except OSError:
#             if os.path.exists(self.sock_path):
#                 raise
#
#         self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#
#         self.sock.bind(self.sock_path)
#
#         self.sock.listen(1)
#
#         print(f'Server listening on {self.sock_path}...')
#
#         while True:
#             # Wait for a client to connect
#             conn, addr = self.sock.accept()
#             print(f'Connected by {addr}')
#
#             data = conn.recv(1024)
#
#             if not data:
#                 conn.close()
#                 continue
#
#             msg = DtoVol.deserialize(data)
#             print(f'Received data: {msg.getNombreDePlaceDispo, msg.getPrix, msg.getReferance}')
#
#             conn.close()
#
#     def stop(self):
#         os.unlink(self.sock_path)
#         self.sock.close()

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
            os.unlink(self.socket_file)  # Remove any previous socket file
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

