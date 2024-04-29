import socket
import threading

PORT = 5050
SERVER_IP = "127.0.0.1"
ADDR = (SERVER_IP, PORT)
DISCONNECT_MSG = "disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def receive_client(conn, addr):
    print("CLIENT CONNECTED:", addr)
    
    connected = True
    while connected:
        msg = conn.recv(1024).decode()  # Specify the maximum number of bytes to receive
        if msg:
            print(f"[{addr}] {msg}")
            if msg == DISCONNECT_MSG:
                connected = False
            response="hello from server!"
            rsp=response.encode()
            conn.send(rsp)
    
    conn.close()


def startserver():
    server.listen()
    print("SERVER IS STARTING AT:", SERVER_IP)
    while True:
        conn, addr = server.accept()
        server.listen()
        thread = threading.Thread(target=receive_client, args=(conn, addr))
        thread.start()
        print("ACTIVE CONNECTIONS TO THE SERVER ARE:", threading.active_count()-1)


startserver()