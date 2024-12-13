# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリ
WORKDIR /app

# 必要なファイルをコピー
COPY server.py /app/

# Pythonでサーバを実行
CMD ["python", "server.py"]
