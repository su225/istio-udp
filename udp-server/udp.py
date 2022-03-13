import os
import socket

address = '0.0.0.0'
port = int(os.environ['SERVER_PORT'])
version = os.environ['SERVER_VERSION']
buffersize = 1024

socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socket.bind((address, port))

print('listening on %s:%d' % (address, port))

while True:
    bytes_and_addr = socket.recvfrom(buffersize)
    message = bytes_and_addr[0]
    reply_addr = bytes_and_addr[1]
    print("received from %s: %s" % (reply_addr, message))
    reply = str.encode(('%s:%s' % (version, message)).rstrip())
    socket.sendto(reply, reply_addr)