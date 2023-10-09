import threading
import socket

clients = []

print("\n Servidor conectado :)  \n")
print(" Inicie o cliente   \n")

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('\nServidor não conectado :( \n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target = tratarMensagem, args = [client])
        thread.start()

def tratarMensagem(client):
    while True:
        try:
            mensagem = client.recv(2048)
            enviarMensagem(mensagem, client)
        except:
            deleteClient(client)
            break

def enviarMensagem(mensagem, client):
        try:
            client.send(mensagem)
        except:
            deleteClient(client)

def deleteClient(client):
    clients.remove(client)

main()
