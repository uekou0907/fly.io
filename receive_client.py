import socket
import pickle
from send_client import GameObject
# サーバのホストとポート
server_address = ('localhost', 12345)

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

while True:
    # データを受信
    data, addr = sock.recvfrom(4096)
    
    # 受信したデータを復元
    game_object = pickle.loads(data)
    
    # 受け取ったオブジェクトを表示
    print(f"Received object: {game_object.name} at {game_object.position} from {addr}")
