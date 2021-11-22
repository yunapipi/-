# 必要モジュールをインポートする
import sqlite3

# データベースに接続する
conn = sqlite3.connect('data.db')
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE TABLE users(id, username, hash, timestamp)''')
conn.close()