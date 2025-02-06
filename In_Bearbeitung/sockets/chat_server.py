"""
Chat Client
Phillip
Jan 2025
"""

import socket
import threading
from doctest import master

PORT = 61111
HOST = '127.0.0.1'
threads = []


class Client(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.conn = conn
        self.addr = addr
        self.client_name = self.conn.recv(1024).decode()
        self.relay_message(f"{self.client_name} has joined the chat".encode())

    def run(self):
        print(f'Connected by {self.client_name} using {addr}')
        self.chat()


    def chat(self):
        while True:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                if data == b"end":
                    break

                print('Received from client', repr(data))
                self.relay_message(data)
            except (ConnectionError, ConnectionAbortedError, ConnectionResetError):
                break

        print(f"{self.client_name} disconnected")
        self.relay_message(f"{self.client_name} has left the chat".encode())
        self.conn.close()
        threads.remove(self)

    def relay_message(self, message):
        for thread in threads:
            if thread != self:
                thread.conn.sendall(message)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Server is listening on port", PORT)
while True:
    try:
        conn, addr = s.accept()
        threads.append(Client(conn, addr))
        for thread in threads:
            if not thread.is_alive():
                thread.start()

    except (KeyboardInterrupt, ConnectionError, IndexError) as e:
        if e == IndexError:
           pass
        else:
            print("Server shutting down")
            break
s.close()