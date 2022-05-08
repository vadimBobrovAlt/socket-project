
import socket


def server(port, listen_count):
    server_socket = socket.socket()
    server_socket.bind((socket.gethostname(), port))
    server_socket.listen(listen_count)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()


if __name__ == '__main__':
    server(5001, 2)




