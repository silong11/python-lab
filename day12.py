import numpy as np
import time

weights = []
with open("logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        try:
            weights.append(float(parts[1]))
        except (ValueError, IndexError):
            print(f"跳过坏行：{line.strip()}")

arr = np.array(weights)

print(f"条数 {len(arr)}，形状 {arr.shape}")
print(f"平均 {arr.mean():.2f} kg")
print(f"最高 {arr.max():.1f} kg，最低 {arr.min():.1f} kg")
print(f"标准差 {arr.std():.2f} kg")
print(f"累计增重 {arr[-1] - arr[0]:.1f} kg")

above = arr[arr > arr.mean()]
print(f"高于平均 {len(above)} 天：{above}")

big = np.random.rand(1000000)
t0 = time.perf_counter()
total = 0.0
for x in big:
    total = total + x
t1 = time.perf_counter()
print(f"100 万条 for 循环：{(t1 - t0) * 1000:.0f} 毫秒")

t2 = time.perf_counter()
m = big.mean()
print(f"100 万条 numpy：{(time.perf_counter() - t2) * 1000:.2f} 毫秒")
print(f"两种算法结果是否一致：{abs(m - total / len(big)) < 1e-9}")