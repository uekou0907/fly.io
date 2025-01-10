import os
import socket
import pickle
import logging

logging.basicConfig(level=logging.INFO)
print("aa")
# ホストとポートの設定
host = ""  # 空文字を指定して、全てのインターフェースでリッスンする
port = int(os.environ.get('PORT', 80))  # Fly.ioの環境で自動的に設定されるポートを使用

# ソケットの作成（TCP）
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))  # hostを空文字にすることで全てのインターフェースにバインド
sock.listen(5)  # 最大接続待ち数を設定
logging.info("Server started successfully")
print(f"Server is running on {host}:{port}")

while True:
    # クライアントからの接続を受け付ける
    conn, addr = sock.accept()
    print(f"Connected by {addr}")

    try:
        # データを受信
        data = conn.recv(4096)
        if not data:
            break

        # 受信したデータをデシリアライズ
        game_object = pickle.loads(data)
        print(f"Received object: {game_object.name} at {game_object.position} from {addr}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # 接続を閉じる
        conn.close()
