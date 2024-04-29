import socket

PORT=5050
SERVER_IP="127.0.0.1"
disconnect_mssg="disconnect"
ADDR=(SERVER_IP,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(message):
    msg=message.encode()
    client.send(msg)
    response=client.recv(1024).decode()
    print(f"SERVER RESPONSE:",{response})

while True:
    send_message('hello')