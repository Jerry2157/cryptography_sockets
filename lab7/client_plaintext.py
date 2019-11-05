import socket
import sys
from Crypto.Cipher import DES
import time
import random
import string

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast



#HOST, PORT = "10.48.107.196", 3000
HOST, PORT = "localhost", 3000
data = " ".join(sys.argv[1:])
data = "hola, soy jerry2"


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    start = time.time()

    # Connect to server and send data
    sock.connect((HOST, PORT))

    #obj = DES.new('abcdefgh', DES.MODE_ECB)
    plain = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    #ciph=obj.encrypt(plain + '...')
    


    #sock.sendall(ciph)
    sock.sendall(bytes(plain, "utf-8"))

    end = time.time()
    print('tiempo en encriptar: ' + str(end - start) + 'seg.')

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

#print("Sent:     {}".format(str(ciph)))
print("Sent:     {}".format(plain))
print("Received: {}".format(received))

