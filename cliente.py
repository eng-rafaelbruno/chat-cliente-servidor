import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receber():
    while True:
        try:
            mensagem = client.recv(1024).decode()

            if mensagem == "NOME":
                client.send(nome.encode())
            else:
                chat.config(state="normal")
                chat.insert(tk.END, mensagem + "\n")
                chat.config(state="disabled")
                chat.yview(tk.END)

        except:
            break


def enviar():
    mensagem = entrada.get()
    texto = f"{nome}: {mensagem}"

    client.send(texto.encode())
    entrada.delete(0, tk.END)


# login no terminal
nome = input("Digite seu nome: ")

# interface
janela = tk.Tk()
janela.title("Chat Python")
janela.geometry("500x600")

chat = ScrolledText(janela, state="disabled")
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entrada = tk.Entry(janela)
entrada.pack(padx=10, pady=10, fill=tk.X)

entrada.bind("<Return>", lambda event: enviar())

botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack(pady=5)

thread = threading.Thread(target=receber)
thread.daemon = True
thread.start()

janela.mainloop()