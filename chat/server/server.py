import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000

clients = []
nombres = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise Exception("Cliente desconectado")
            broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                nombre = nombres[index]

                clients.remove(client)
                nombres.remove(nombre)
                client.close()

                broadcast(f"{nombre} salió del chat.".encode("utf-8"))
                print(f"{nombre} se desconectó.")
            break

def receive_connections():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Servidor corriendo en el puerto {PORT}...")

    while True:
        client, address = server.accept()
        print(f"Conectado con {address}")

        client.send("NOMBRE".encode("utf-8"))
        nombre = client.recv(1024).decode("utf-8")

        nombres.append(nombre)
        clients.append(client)

        print(f"Nombre del usuario: {nombre}")
        broadcast(f"{nombre} se unió al chat.".encode("utf-8"))
        client.send("Conectado al servidor.".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()