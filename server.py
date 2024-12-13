import socket
import pickle

# Fly.ioで使用するホストとポート
host = "0.0.0.0"
port = 12345

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print(f"Server is running on {host}:{port}")

while True:
    data, addr = sock.recvfrom(4096)
    game_object = pickle.loads(data)
    print(f"Received object: {game_object.name} at {game_object.position} from {addr}")
