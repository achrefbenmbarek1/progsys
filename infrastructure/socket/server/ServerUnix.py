import socket
import os
import sys
# from gestionDesVols.dto.DtoVol import DtoVol
from .Server import Server

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from dto.DtoVol import DtoVol

class ServerUnix(Server):
    def __init__(self, sock_path):
        self.sock_path = sock_path

    def start(self):
        # Make sure the socket file doesn't already exist
        try:
            os.unlink(self.sock_path)
        except OSError:
            if os.path.exists(self.sock_path):
                raise

        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        self.sock.bind(self.sock_path)

        self.sock.listen(1)

        print(f'Server listening on {self.sock_path}...')

        while True:
            # Wait for a client to connect
            conn, addr = self.sock.accept()
            print(f'Connected by {addr}')

            data = conn.recv(1024)

            if not data:
                conn.close()
                continue

            msg = DtoVol.deserialize(data)
            print(f'Received data: {msg.getNombreDePlaceDispo, msg.getPrix, msg.getReferance}')

            conn.close()

    def stop(self):
        os.unlink(self.sock_path)
        self.sock.close()
