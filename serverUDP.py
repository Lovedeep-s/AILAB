import socket

PORT = 5050
SERVER_IP = "127.0.0.1"
ADDR = (SERVER_IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

print("SERVER IS STARTING AT:", SERVER_IP)

while True:
    data, addr = server.recvfrom(1024)
    print("CLIENT CONNECTED:", addr)
    print(f"[{addr}] {data.decode()}")
    response = "hello from server!"
    server.sendto(response.encode(), addr)
