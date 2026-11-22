import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("logs.csv")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(df["date"], df["weight"], marker="o")
axes[0].set_title("体重变化")
axes[0].set_xlabel("日期")
axes[0].set_ylabel("体重 kg")

axes[1].bar(df["date"], df["kcal"], color="steelblue")
axes[1].set_title("每日热量")
axes[1].set_xlabel("日期")
axes[1].set_ylabel("kcal")
axes[1].axhline(df["kcal"].mean(), color="red", linestyle="--", label="平均线")
axes[1].legend(loc="upper left")

plt.tight_layout()
plt.savefig("day16.png", dpi=150)
plt.show()