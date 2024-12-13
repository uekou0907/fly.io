import os
import socket
import pickle

host = "0.0.0.0"
port = int(os.environ.get('PORT', 12345))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
print(f"Server is running on {host}:{port}")

while True:
    data, addr = sock.recvfrom(4096)
    game_object = pickle.loads(data)
    print(f"Received object: {game_object.name} at {game_object.position} from {addr}")