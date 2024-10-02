# Socket Programming Client File
import socket
import pyautogui
import time


class Client:
    def __init__(self, port, address):
        self.port = port
        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.sock.connect((self.address, self.port))
            print('Connected to server')
        except Exception as e:
            print(f'Failed to connect to server: {e}')

    def send_message(self, message):
        try:
            self.sock.send(message.encode())
            print('Message sent')
        except Exception as e:
            print(f'Error sending message: {e}')

    def send_update(self):
        try:
            pyautogui.screenshot('sample.png')
            file = open('sample.png', 'rb')
            file_data = file.read(2048)
            while file_data:
                self.sock.send(file_data)
                file_data = file.read(2048)
            print('File sent')
            file.close()
        except Exception as e:
            print(f'Error sending file: {e}')

    def receive_update(self):
        print('Ready to receive update')
        try:
            while True:
                msg = self.sock.recv(1024)
                if not msg:
                    break
                print(msg.decode('utf-8'))
        except Exception as e:
            print(f'Error receiving message: {e}')
        finally:
            self.sock.close()
            print('Socket closed')
