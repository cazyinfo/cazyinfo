#
# export PYTHONIOENCODING=utf8  # これしないと文字化け
# export LC_ALL="ja_JP.UTF-8"   # これも重要そう locale コマンドで確認

import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('1.csv', encoding='utf-8')

# 取引種別が 'bid' の場合の行をフィルタリング
bid_df = df[df['取引種別'] == 'bid']

ask_df = df[df['取引種別'] == 'ask']

# 価格と数量の総和を計算
bid_t = (bid_df['価格'] * bid_df['数量']).sum()
ask_t = (ask_df['価格'] * ask_df['数量']).sum()

print("bid 価格 * 数量 の総和:", bid_t)
print("ask 価格 * 数量 の総和:", ask_t)
su = 0; currrent_price=0
now_su = su * currrent_price
print("利益:", ask_t - bid_t + now_su)  # now_su: 現在保持しているコイン額 
