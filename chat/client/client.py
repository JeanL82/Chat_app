import socket
import threading 



HOST = "10.0.0.90"
PORT = 5000
name = input("Ingrese su nombre: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "NOMBRE":
                client.send((name).encode("utf-8"))
            
            else:
                print(message)
        except:
            print("Error al recibir mensaje del servidor.")
            client.close()
            break

def send_messages():
    while True:
        try:
            text = input()
            if message.lower() == "salir":
                print("Saliendo del chat...")
                client.close()
                break
            message = f"{name}: {text}"
            client.send(message.encode("utf-8"))
        except:
            print("Error al enviar mensaje al servidor.")
            client.close()
            break





receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
