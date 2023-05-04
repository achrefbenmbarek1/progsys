import sys
import os
from infrastructure.socket.client.Client import Client
from infrastructure.socket.server.Server import Server
from infrastructure.socket.socketFactory.FactorySocketUnixImp import FactorySocket, FactorySocketUnixImp
from infrastructure.socket.socketFactory.FactorySocketTcpImp import FactorySocketTcpImp
from infrastructure.socket.socketFactory.FactorySocketUdpImp import FactorySocketUdpImp
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
        dtoReferance = DtoReferance("dhf", "vol","get")
        socketFactory:FactorySocket = FactorySocketUnixImp(sock_path, dtoReferance)
        server:Server = socketFactory.getServer()
        server.start()
        server.stop()

    elif mode == 'server' and protocol == "tcp" :
        dtoReferance = DtoReferance("dhf", "vol","get")
        factory:FactorySocket = FactorySocketTcpImp(ipAddress, port,dtoReferance)
        server:Server = factory.getServer()
        server.start()
        server.stop()

    elif mode == 'server' and protocol == "udp" :
        dtoReferance = DtoReferance("dhf", "vol","get")
        factory:FactorySocket = FactorySocketTcpImp(ipAddress, port, dtoReferance)
        server:Server = factory.getServer()
        server.start()
        server.stop()

    elif mode == 'client':

        while True:
            print("Choisissez une option :")
            print("1. Consulter la liste des vols")
            print("2. Consulter la facture d'une agence")
            print("3. Consulter l'historique des transactions")
            print("4. Réaliser des transactions")
            print("5. Quitter")
            choix = input()

            if choix == "1":
                os.system('clear')
                if protocol == 'unix':
                    reference = input("saisir la reference du vol")
                    dtoReferance = DtoReferance(reference, "vol", "get")
                    factory:FactorySocket = FactorySocketUnixImp(sock_path, dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                elif protocol == 'tcp':
                    reference = input("saisir la reference du vol")
                    # dtoReferance = DtoReferance("dhf", "vol", "get")
                    dtoReferance = DtoReferance(reference, "vol", "get")
                    factory:FactorySocket = FactorySocketTcpImp(ipAddress, port, dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                elif protocol == 'udp':
                    dtoReferance = DtoReferance("dhf", "vol","get")
                    factory:FactorySocket = FactorySocketUdpImp(ipAddress, port,dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                else:
                    print('invalid protocol')

            elif choix == "2":
                os.system('clear')
                if protocol == 'unix':
                    reference = input("saisir la reference de la facture")
                    dtoReferance = DtoReferance(reference, "facture", "get")
                    factory:FactorySocket = FactorySocketUnixImp(sock_path, dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                elif protocol == 'tcp':
                    reference = input("saisir la reference de la facture")
                    dtoReferance = DtoReferance(reference, "facture", "get")
                    factory:FactorySocket = FactorySocketTcpImp(ipAddress, port, dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                elif protocol == 'udp':
                    dtoReferance = DtoReferance("dhf", "vol","get")
                    factory:FactorySocket = FactorySocketUdpImp(ipAddress, port,dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                else:
                    print('invalid protocol')

            elif choix == "3":
                os.system('clear')
                if protocol == 'unix':
                    dtoReferance = DtoReferance("dummyField", "transactionHistory", "get")
                    factory:FactorySocket = FactorySocketUnixImp(sock_path, dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                elif protocol == 'tcp':
                    dtoReferance = DtoReferance("dummyField", "transactionHistory", "get")
                    factory:FactorySocket = FactorySocketTcpImp(ipAddress, port, dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                elif protocol == 'udp':
                    dtoReferance = DtoReferance("dhf", "vol","get")
                    factory:FactorySocket = FactorySocketUdpImp(ipAddress, port,dtoReferance)
                    client:Client = factory.getClient()
                    client.send()

                else:
                    print('invalid protocol')

            elif choix == "4":
                break
            elif choix == "5":
                break
            else:
                print("Choix invalide. Veuillez entrer un chiffre entre 1 et 5.")
       
    else:
        print('Invalid mode. Use "server" or "client" and precise the protocol.')
        sys.exit(1)

if __name__ == '__main__':
    main()

