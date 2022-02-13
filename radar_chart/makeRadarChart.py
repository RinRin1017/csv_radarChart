# レーダーチャートのテストプログラム
# csvからの読み込みなし
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

data = pd.DataFrame({
    "カルシウム": [1.5, 0.5],
    "鉄": [1.8, 0.9],
    "ビタミンA": [1.5, 0.8],
    "ビタミンB1": [1.2, 0.4],
    "ビタミンB2": [2.1, 0.7],
    "ナイアシン": [1, 0.3],
    "ビタミンC": [1.5, 0.7],
    "ビタミンD": [2, 0.8]
})
data.index = ["コーンフレーク", "パン"]

# dataの表示
data

# cnum: ラベルの数(headerの数)
cnum = len(data.columns)
cnum

# angles 角度
angles = np.linspace(0, 2 * np.pi, cnum + 1)
angles

# cvalues コンフレークの値
# pvalues: パンの値
cvalues = np.concatenate((data.loc["コーンフレーク"], [data.loc["コーンフレーク"][0]]))
pvalues = np.concatenate((data.loc["パン"], [data.loc["パン"][0]]))
print(cvalues)
print(pvalues)

# labels : ラベル名
labels = data.columns
data.columns

# 作図
fig = plt.figure(figsize=(10, 10))  # グラフの箱準備
ax = fig.add_subplot(2, 2, 1, polar=True)  # 極座標系を作る
plt.subplots_adjust(wspace=0.4, hspace=0.6)

# 見映えを修正
# 北を視点にする
ax.set_theta_zero_location("N")
# 時計回りにする
ax.set_theta_direction(-1)

# ラベルの書き込みとメモリの最大値設定
ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
ax.set_rlim(0, 3)

# コーンフレーク部分
ax.plot(angles, cvalues, "o-", label="コンフレーク")
ax.fill(angles, cvalues, alpha=0.25)

# パン部分
ax.plot(angles, pvalues, "o-", label="パン")
ax.fill(angles, pvalues, alpha=0.25)

# ax.legend(loc="lower right")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

ax.set_title('パンとコンフレーク', loc='center', pad=20)

ax = fig.add_subplot(2, 2, 2, polar=True)  # 極座標系を作る

# 見映えを修正
# 北を視点にする
ax.set_theta_zero_location("N")
# 時計回りにする
ax.set_theta_direction(-1)

# ラベルの書き込みとメモリの最大値設定
ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
ax.set_rlim(0, 3)

# コーンフレーク部分
ax.plot(angles, cvalues, "o-", label="コンフレーク")
ax.fill(angles, cvalues, alpha=0.25)

# パン部分
ax.plot(angles, pvalues, "o-", label="パン")
ax.fill(angles, pvalues, alpha=0.25)
ax.legend(loc="lower right")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

plt.show()
