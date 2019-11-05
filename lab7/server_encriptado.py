import socket
from Crypto.Cipher import DES
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from des import DesKey
from Crypto.Cipher import PKCS1_OAEP

random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()

def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

def importKey(externKey):
   return RSA.importKey(externKey)

code = 'jerrypassphrase'




simetric_key = ""
flag_have_simetric = False

flag_pb = False
flag_handshake = False

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
while True:
    if flag_handshake == False:
        rcvdData = c.recv(1024).decode()
        if rcvdData == 'handshake' and flag_pb == False:
            print('enter handshake')
            c.send('next_pb'.encode())
            flag_pb = True
        elif flag_pb == True:
            print('enter pb')
            c.send(public_key.exportKey())
            flag_handshake = True
    elif flag_handshake == True and flag_have_simetric == False:
        print("entre a pedir encrypted")
        simetric_from_client = c.recv(1024)
        print(decrypt(simetric_from_client,private_key).decode())
        simetric_key = decrypt(simetric_from_client,private_key).decode()
        flag_have_simetric = True
    elif flag_handshake == True and flag_have_simetric == True:
        key0 = DesKey(simetric_key.encode())
        message_encrypted = key0.decrypt(c.recv(1024), padding=True)
        print(message_encrypted.decode())
        pass
        
    sendData = input("continue?: ")
    c.send(sendData.encode())
c.close()