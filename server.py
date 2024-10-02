# Socket Programming Server File
import time
import socket

class Server:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.address = socket.gethostname()
        self.port = port
        self.sock.bind(('', self.port))
        print('Set as server')

    def receive_update(self):
        self.sock.listen()
        print(f'Server listening on port {self.port}')
        self.client_sock, self.client_addr = self.sock.accept()
        print(f'Connection from {self.client_addr}')

        # Receive image data
        with open('server_img.png', 'wb') as file:
            print('Gathering image...')
            while True:
                data = self.client_sock.recv(1024)
                if not data:
                    break
                file.write(data)

        print('Image received and saved as server_img.png')
        self.client_sock.close()  # Close client socket after receiving
        print('Client socket closed')

    def send_update(self):
        # Placeholder for sending updates to the client
        try:
            message = "Hey!, this is an update!"
            self.client_sock.sendall(message.encode())
            print('Update message sent to client')
        except Exception as e:
            print(f'Error sending update: {e}')

# Create and start the server
my_server = Server(6060)

while True:
    my_server.receive_update()
    my_server.send_update()
