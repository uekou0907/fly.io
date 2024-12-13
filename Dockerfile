# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# アプリケーションの依存関係をインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# 使用するポート（UDP）を開放
EXPOSE 12345/udp  # UDP通信に使用するポートを指定 (例: 12345)

# アプリケーションを起動するコマンドを指定
CMD ["python", "server.py"]
