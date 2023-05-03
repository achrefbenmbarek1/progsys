import sys
from infrastructure.socket.client.Client import Client
from infrastructure.socket.server.Server import Server
from infrastructure.socket.socketFactory.FactorySocketUnixImp import FactorySocket, FactorySocketUnixImp
from infrastructure.socket.socketFactory.FactorySocketTcpImp import FactorySocketTcpImp
from infrastructure.socket.socketFactory.FactorySocketUdpImp import FactorySocketUdpImp
from infrastructure.dto.DtoVol import DtoVol
from infrastructure.dto.DtoReferance import DtoReferance

def main():
    if len(sys.argv) < 3:
            print('Usage: python main.py [server |client] protocol(tcp, udp, unix)')
            sys.exit(1)

    mode = sys.argv[1]
    protocol = sys.argv[2]

    ipAddress = "192.168.100.6"
    # ipAddress = "127.0.0.1"
    port = 5104

    sock_path = '/tmp/mysocket'

    if mode == 'server' and protocol == "unix" :
        socketFactory:FactorySocket = FactorySocketUnixImp(sock_path)
        server:Server = socketFactory.getServer()
        server.start()
        server.stop()

    elif mode == 'server' and protocol == "tcp" :
        # dtoVol = DtoVol("dhff",5,3.1,"dhf")
        dtoReferance = DtoReferance("dhf", "vol","get")
        factory:FactorySocket = FactorySocketTcpImp(ipAddress, port,dtoReferance)
        server:Server = factory.getServer()
        server.start()
        server.stop()

    elif mode == 'server' and protocol == "udp" :
        # dtoVol = DtoVol("dhff",5,3.1,"dhf")
        dtoReferance = DtoReferance("dhf", "vol","get")
        factory:FactorySocket = FactorySocketTcpImp(ipAddress, port, dtoReferance)
        server:Server = factory.getServer()
        server.start()
        server.stop()

    elif mode == 'client' and protocol == 'unix':
        factory:FactorySocket = FactorySocketUnixImp(sock_path)
        client:Client = factory.getClient()
        client.send()

    elif mode == 'client' and protocol == 'tcp':
        # dtoVol = DtoVol("dhff",5,3.1,"dhf")
        dtoReferance = DtoReferance("dhf", "vol", "get")
        factory:FactorySocket = FactorySocketTcpImp(ipAddress, port, dtoReferance)
        client:Client = factory.getClient()
        client.send()

    elif mode == 'client' and protocol == 'udp':
        dtoReferance = DtoReferance("dhf", "vol","get")
        factory:FactorySocket = FactorySocketUdpImp(ipAddress, port,dtoReferance)
        client:Client = factory.getClient()
        client.send()
        
    else:
        print('Invalid mode. Use "server" or "client" and precise the protocol.')
        sys.exit(1)

if __name__ == '__main__':
    main()

