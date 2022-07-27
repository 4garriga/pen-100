#!/usr/bin/python3

import socket

HOST = socket.gethostname()
PORT = 8080
SIZE = 1024
N = 4

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    try:
        server.bind((HOST, PORT))
    except ConnectionRefusedError:
        print(f'Binding to port {PORT} refused!')
    else:
        server.listen(N)
        print(f'Server listening for up to {N} clients')
        conn, addr = server.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(SIZE)
                conn.send(b'connection established')
