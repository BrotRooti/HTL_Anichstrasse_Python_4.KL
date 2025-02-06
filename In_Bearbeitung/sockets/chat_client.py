"""
Chat Client
Phillip
Jan 2025
"""

import random
import socket
import threading


color_list = ["\033[1;31m", "\033[1;34m", "\033[1;36m", "\033[0;32m"]
reset_color = "\033[0m"

PORT = 61111


def receive_messages():
    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            print(f"{data.decode()}")
        except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
            break


user_name = input("Enter your user name: ")
user_color = random.choice(color_list)

try:
    server = input("Enter the server IP you want to connect to: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, PORT))
except (ConnectionRefusedError, ConnectionError, socket.gaierror, KeyboardInterrupt):
    print("Could not connect to server")
    exit()

print("welcome to the chat server, please type what you want and 'end' to quit")
s.send(user_name.encode())


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()


while True:
    try:
        data = input()
        if data == "end":
            break
        s.sendall(f"{user_color}{user_name}: {data} {reset_color}".encode())

    except (ConnectionResetError, ConnectionError, ConnectionAbortedError, KeyboardInterrupt) as e:
        if e == KeyboardInterrupt:
            print("You have left the chat")
        else:
            print("Connection error")
        break


try:
    s.send(b"end")
    print("cleaning up ...")
    s.close()
except ConnectionResetError:
    print("Server has disconnected")
    s.close()
    exit()