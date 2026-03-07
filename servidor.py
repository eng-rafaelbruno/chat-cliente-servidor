import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clientes = []
nomes = []

print("Servidor iniciado...")
print("Aguardando conexões...")


def broadcast(mensagem):
    for cliente in clientes:
        cliente.send(mensagem)


def handle_cliente(conn):
    while True:
        try:
            mensagem = conn.recv(1024)
            broadcast(mensagem)
        except:
            index = clientes.index(conn)
            clientes.remove(conn)

            nome = nomes[index]
            nomes.remove(nome)

            broadcast(f"{nome} saiu do chat".encode())

            conn.close()
            break


while True:
    conn, addr = server.accept()

    print("Cliente conectado:", addr)

    conn.send("NOME".encode())
    nome = conn.recv(1024).decode()

    nomes.append(nome)
    clientes.append(conn)

    print(nome, "entrou no chat")

    broadcast(f"{nome} entrou no chat".encode())

    thread = threading.Thread(target=handle_cliente, args=(conn,))
    thread.start()