#!/usr/bin/python3
import socket


def client(host: str, port: int, size: int) -> bytes:
    """Connects to host on port and prints message."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((host, port))
        except ConnectionRefusedError:
            print(f"Connect to {host} on port {port} refused!")
        else:
            msg = client.recv(size)
            
            return msg

def echo_client(host: str, port: int, size: int) -> bytes:
    """Sends received bytes to server."""
    
    response = b''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((host, port))
        except ConnectionRefusedError:
            print(f'Connection to {host}:{port} refused!')
        else:
            while True:
                msg = client.recv(size)
                if isinstance(msg, bytes) and len(msg) > 0:
                    print(msg.decode('ascii').replace('\r\n', ''))
                    response += msg
                    try:
                        client.sendall(msg)
                    except BrokenPipeError:
                        break
                else:
                    break

    return response
