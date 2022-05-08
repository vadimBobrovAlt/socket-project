
import socket


def client():
    client_socket = socket.socket()
    client_socket.connect((socket.gethostname(), 5001))
    message = input(" -> ")
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input(" -> ")
    client_socket.close()


if __name__ == '__main__':
    client()


