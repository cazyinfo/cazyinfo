#
# export PYTHONIOENCODING=utf8  # これしないと文字化け
# export LC_ALL="ja_JP.UTF-8"   # これも重要そう locale コマンドで確認

import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('1.csv', encoding='utf-8')

# 取引種別が 'bid' の場合の行をフィルタリング
bid_df = df[df['取引種別'] == 'bid']

# 価格と数量の総和を計算
total_value = (bid_df['価格'] * bid_df['数量']).sum()

print("価格 * 数量 の総和:", total_value)
