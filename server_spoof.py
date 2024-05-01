import socket

HOST = '10.0.2.15' 
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

while True:
    data, addr = server.recvfrom(1024)
    print(f"Received data from {addr}: {data.decode()}")
