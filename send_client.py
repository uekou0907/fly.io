import socket
import pickle

class GameObject:
    def __init__(self, name, position):
        self.name = name
        self.position = position

# サーバのホストとポート
server_address = ('66.241.125.159', 80)

# ソケットの作成（TCP）
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # サーバーに接続
    sock.connect(server_address)
    print(f"Connected to server at {server_address}")

    # GameObjectを作成
    game_object = GameObject("Player1", (100, 200))

    # オブジェクトをシリアライズして送信
    data = pickle.dumps(game_object)
    sock.sendall(data)
    print("Data sent successfully")

finally:
    # ソケットを閉じる
    sock.close()
