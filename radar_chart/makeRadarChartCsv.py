# CSVから読み込んだデータからレーダーチャートを作成する
# 1.データは1列目がラベルになっている
# 2.1列目はインデックスになっていること

import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# csvデータの読み込み(個人データ)
read_rows = 20
personal_data = pd.read_csv('../15819105_moriyama.csv', index_col=0, nrows=read_rows)
personal_data

# csvデータの読み込み(平均データ)
average_data = pd.read_csv('../average.csv', index_col=0, nrows=read_rows)
average_data

# cnum: ラベルの数(scaleの数)
cnum = len(personal_data.columns)
cnum

# angles 角度
angles = np.linspace(0, 2 * np.pi, cnum + 1)
angles

# 個人データ用の配列の初期化
pvalues = []

# 個人用データを配列に格納
for i in range(read_rows):
    value = np.concatenate((personal_data.loc[i + 1], [personal_data.loc[i + 1][0]]))
    pvalues.append(value)
# pvalues

# 平均データの格納
avalues = []
for i in range(read_rows):
    value = np.concatenate((average_data.loc[i + 1], [average_data.loc[i + 1][0]]))
    avalues.append(value)
# avalues

# labels : ラベル名(各列名)
labels = personal_data.columns
# labels

# 作図を繰り返す
fig = plt.figure(figsize=(20, 20))  # グラフの箱準備
plt.subplots_adjust(wspace=0.4, hspace=0.6)  # グラフ間の幅

for i in range(read_rows):
    ax = fig.add_subplot(5, 4, i + 1, polar=True)  # 極座標系を作る
    # 見映えを修正
    # 北を視点にする
    ax.set_theta_zero_location("N")
    # 時計回りにする
    ax.set_theta_direction(-1)
    # ラベルの書き込みとメモリの最大値設定
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
    ax.set_rlim(-2, 2)

    # 個人データ部分
    ax.plot(angles, pvalues[0], "o-", label="個人")
    ax.fill(angles, pvalues[0], alpha=0.25)

    # 平均データ部分
    ax.plot(angles, avalues[i], "o-", label="平均")
    ax.fill(angles, avalues[i], alpha=0.25)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

    g_title = "音源" + str(i + 1)
    ax.set_title(g_title, loc='center', pad=10)


fig.savefig("img_test2.png")
plt.show()



