import socketserver
from Crypto.Cipher import DES
import time

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        
        print("{} wrote:".format(self.client_address[0]))
        start = time.time()
        #obj=DES.new('abcdefgh', DES.MODE_ECB)
        #a = obj.decrypt(self.data)
        #print(str(a))
        print(str(self.data))
        end = time.time()
        print('tiempo en desencriptar: ' + str(end - start) + 'seg.')
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
        self.request.sendall(bytes("Recibí tu mensaje", "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 3000

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()