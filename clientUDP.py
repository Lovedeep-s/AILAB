import socket

PORT = 5050
SERVER_IP = "127.0.0.1"
ADDR = (SERVER_IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_message(message):
    msg = message.encode()
    client.sendto(msg, ADDR)
    response, _ = client.recvfrom(1024)
    print(f"SERVER RESPONSE: {response.decode()}")

while True:
    send_message('hello')
