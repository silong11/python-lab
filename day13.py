import numpy as np

rows = []
with open("logs.txt", "r", encoding="utf-8") as f:
    for line  in f:
        parts = line.strip().split(",")
        try:
            rows.append([float(parts[1]), float(parts[2])])
        except (ValueError, IndexError):
            print(f"跳过坏行：{line.strip()}")

m = np.array(rows)
weight = m[:,0]
kcal = m[:,1]

print(f"形状 {m.shape}")
print(f"体重：均值 {weight.mean():.2f},最高 {weight.max():.1f}, 最低 {weight.min():.1f}")
print(f"热量：均值 {kcal.mean():.0f}, 合计 {kcal.sum():.0f}")
print(f"按列统计 axis=0: {m.mean(axis=0)}")

share = kcal /kcal.sum()
print(f"每天热量占比： {np.round(share * 100, 1)}%")

high = m[weight > weight.mean()]
print(f"高于平均体重的天数： {len(high)}")
print(f"这些天的热量合计： {high[:,1].sum():.0f}")