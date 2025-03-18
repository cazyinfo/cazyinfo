sql = "SELECT * FROM users WHERE age >= %(age)s AND sex = %(sex)s"
params = {"age": 40, "sex": "male"}

# SQL文字列を展開して取得
sql_expanded = sql % params

print(sql_expanded)

"""
import psycopg2  # PostgreSQLデータベース用のライブラリを例として使用

# データベース接続
conn = psycopg2.connect(database="your_database", user="your_username", password="your_password")
cursor = conn.cursor()

# SQL文とパラメータ
sql = "SELECT * FROM users WHERE age >= %(age)s AND sex = %(sex)s"
params = {"age": 40, "sex": "male"}

# クエリの実行
cursor.execute(sql, params)

# 結果の取得
rows = cursor.fetchall()

# 結果の出力
for row in rows:
    print(row)

# リソースをクリーンアップ
cursor.close()
conn.close()
"""
