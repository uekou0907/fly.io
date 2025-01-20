import socket
import pickle
from send_client import GameObject

# サーバのホストとポート
server_address = ('66.241.125.159', 80)

# ソケットの作成（TCP）
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(server_address)

# サーバーをリッスン状態にする
sock.listen(5)  # 最大接続待ち数を指定
print(f"Server is listening on {server_address}")

while True:
    # クライアントからの接続を受け付ける
    conn, addr = sock.accept()
    print(f"Connected by {addr}")

    try:
        # データを受信
        data = conn.recv(4096)
        if not data:
            break
        
        # 受信したデータを復元
        game_object = pickle.loads(data)
        
        # 受け取ったオブジェクトを表示
        print(f"Received object: {game_object.name} at {game_object.position} from {addr}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # 接続を閉じる
        conn.close()
