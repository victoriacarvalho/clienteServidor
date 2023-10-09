import threading
import socket

def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(('localhost', 7777))
    except:
        return print('\nServidor não iniciado :( \n')

    user = input('Usuário> ')
    print("\n")
    print(user +' conectado(a) ao servidor')

    thread1 = threading.Thread(target = receiveMessages, args = [cliente])
    thread2 = threading.Thread(target = sendMessages, args = [cliente, user])

    thread1.start()
    thread2.start()

def contaVogais(string):
    string = string.lower() 
    vogais = 'aeiou'
    return {i: string.count(i) for i in vogais if i in string}

def contaConsoantes(string):
    string = string.lower() 
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    return {i: string.count(i) for i in consoantes if i in string}

def receiveMessages(server):
    while True:
        try:
            mensagem = server.recv(2048).decode('utf-8')
            print('\n' + mensagem)
        except:
            print('\nNão foi possível manter a conexão :( \n')
            server.close()
            break
            
def inverterString(txt):
  return txt[::-1]

def sendMessages(server, username):
    while True:
        try:
            mensagem = input('\n')
            server.send(f'String digitada: {mensagem}'.encode('utf-8'))
            server.send(f'\n Vogais: {contaVogais(mensagem)}'.encode('utf-8'))
            server.send(f'\n Consoantes: {contaConsoantes(mensagem)}'.encode('utf-8'))
            server.send(f'\n Invertido: {inverterString(mensagem)}'.encode('utf-8'))
            print('\n')
            
        except:
            return


main()