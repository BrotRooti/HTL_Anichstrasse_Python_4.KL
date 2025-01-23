'''
Echo server mit multi threading - ist in der Lage
mit mehr als einem Client gleichzeitig zu sprechen

zweite Uebung fuer Sockets in Python

Mai 2021
Markus
'''

import socket
import threading


# echo function - bekommt die Adresse und den Client-Socket
def echo(conn, addr):
    print('Connected by', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Received from client', repr(data))
        conn.sendall(data)
    conn.close()


HOST = '127.0.0.1'
PORT = 61111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    echo_thread = threading.Thread(target=echo, args=(conn, addr))
    echo_thread.start()

