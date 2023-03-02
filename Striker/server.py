import socket
import threading

ip = 'localhost'
port = 9999

class ClientThread(threading.Thread):

    ip = ip
    port = port

    def __init__(self, clientsocket):

        threading.Thread.__init__(self)
        self.clientsocket = clientsocket

    def run(self):
        response = self.clientsocket.recv(2048).decode()
        if (response.startswith('[') and len(response)>1) or response == ' ':
            print(response)
        else:
            print(response, end='', flush=True)
        self.clientsocket.send(str.encode('response'))

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((ip,port))

while True:
    """
        écoute sur le port 9999
        Le thread permet de gérer plusieurs connexion à la fois
    """
    tcpsock.listen(10)
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(clientsocket)
    newthread.start()