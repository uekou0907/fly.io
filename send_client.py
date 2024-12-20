import socket
import pickle

class GameObject:
    def __init__(self, name, position):
        self.name = name
        self.position = position

# サーバのホストとポート
server_address = ('66.241.125.159', 80)

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# GameObjectを作成
game_object = GameObject("Player1", (100, 200))

# オブジェクトをシリアライズして送信
data = pickle.dumps(game_object)
sock.sendto(data, server_address)
sock.close()
