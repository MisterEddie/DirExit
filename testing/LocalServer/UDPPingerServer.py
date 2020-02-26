
from socket import *
import time

#create UDP socket
#notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
#assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    #receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    #print message
    print(message.decode())

    #capitalize the message from the client
    message = message.upper()
    #server respond
    time.sleep(0)
    serverSocket.sendto(message, address)
