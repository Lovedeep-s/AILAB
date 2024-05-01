import socket

HOST = '10.0.2.15'
PORT = 12345
SPOOFED_IP = '192.168.1.100'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello, server!", (HOST, PORT))

client.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
client.sendto(b"Hello, server!", (HOST, PORT))
