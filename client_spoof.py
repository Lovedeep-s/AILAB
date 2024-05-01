import socket
import struct

def create_ip_header(source_ip, dest_ip):
    version = 4
    ihl = 5
    ttl = 255
    protocol = socket.IPPROTO_UDP
    saddr = socket.inet_aton(source_ip)
    daddr = socket.inet_aton(dest_ip)

    ip_header = struct.pack('!BBHHHBBH4s4s', (version << 4) + ihl, 0, 0, 0, 0, ttl, protocol, 0, saddr, daddr)
    return ip_header

def create_udp_packet(source_ip, dest_ip, source_port, dest_port, data):
    udp_header = struct.pack('!HHHH', source_port, dest_port, 8 + len(data), 0)  # UDP header
    pseudo_header = struct.pack('!4s4sBBH', socket.inet_aton(source_ip), socket.inet_aton(dest_ip), 0, socket.IPPROTO_UDP, len(udp_header) + len(data))  # Pseudo-header for checksum calculation
    udp_checksum = socket.htons(sum(map(int, struct.unpack('!4H', pseudo_header + udp_header + data))))  # UDP checksum

    return udp_header + struct.pack('!H', udp_checksum) + data

source_ip = '192.168.1.100'  # Spoofed source IP address
dest_ip = '127.0.0.1'
source_port = 12345
dest_port = 12345

ip_header = create_ip_header(source_ip, dest_ip)
udp_packet = create_udp_packet(source_ip, dest_ip, source_port, dest_port, b"Hello, server!")

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
s.sendto(ip_header + udp_packet, (dest_ip, dest_port))
