import socket
import random
import string


from Crypto.Cipher import PKCS1_OAEP
import socket
from Crypto.Cipher import DES
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from des import DesKey

randomKey = '-8,13Xh3!g,QUA`'
def randomString(stringLength=16):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#variables
randomKey = randomString(8)
key0 = DesKey(randomKey.encode()) 

s = socket.socket()
s.connect(('127.0.0.1',12345))


next_handhsake = True
next_pb_flag = False
next_pb_deal = False
public_key = 'a'.encode()


def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

def importKey(externKey):
   return RSA.importKey(externKey)

while True:
    if next_handhsake == True:
        s.send('handshake'.encode())
        next_handhsake = False
    elif next_pb_deal == False:
        server_message = ""
        try:
            server_message = s.recv(1024).decode()
            #print(server_message)
        except:
            pass
        if server_message == 'next_pb':
            s.send('give me pb'.encode())
            print('pedi pb')
            next_pb_flag = True
        elif next_pb_flag == True:
            public_key = s.recv(1024)
            a = encrypt(randomKey.encode(),importKey(public_key))
            print(a)
            next_pb_flag = False
            sendData = input("continue?: ")
            s.send(a)
            next_pb_deal = True
    elif next_pb_deal == True:
        sendData = input("Messsage to encrypt and send: ")
        a = key0.encrypt(sendData.encode(), padding=True)
        s.send(a)
        pass
    

    # print ("N:",s.recv(1024).decode())
s.close()