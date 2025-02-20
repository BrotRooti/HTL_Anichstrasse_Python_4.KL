import socket
import multiprocessing as mp

import pickle
import time

HOST = '10.5.5.58'
PORT = 61111


class ClientInterface(mp.Process):
    def __init__(self, conn, addr):
        mp.Process.__init__(self, args=())
        self.conn = conn
        self.addr = addr
        self.partner = None
        self.match_made = False

    def run(self):
        self.match_making()
        #self.receive()

    def match_making(self):
        global clients
        for client in clients:
            if client != self and not client.match_made and client.is_alive():
                self.partner = client
                client.partner = self
                self.match_made = True
                client.match_made = True
                #self.send("match made")
                self.send("o")
                self.game_loop()
                #client.send("match made")
                client.send("x")
                client.game_loop()
                break
        if not self.match_made:
            clients.append(self)
        #while not self.match_made:
            #try:
            #    pass


    def send(self, data):
        data.encode()
        self.conn.send(data)

    def receive(self):
        data = self.conn.recv(1024)
        return data

    def game_loop(self):
        while True:
            data = self.receive()
            if not data:
                break
            self.partner.send(data)
        self.close()

    def close(self):
        self.conn.close()
        clients.remove(self)


clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print("Server is listening on port", PORT)

while True:
    try:
        conn, addr = s.accept()
        clients.append(ClientInterface(conn, addr))
        clients[-1].start()
        print(f"New client connected using IP {clients[-1].addr}, total clients: {len(clients)}")
        #for client in clients:
        #    if not client.is_alive():
        #        client.start()

    except (KeyboardInterrupt, ConnectionError, IndexError, RuntimeError) as e:
        if e == IndexError:
            pass
        else:
            print("Server shutting down")
            print(e)
            s.close()
            break
s.close()
time.sleep(5)