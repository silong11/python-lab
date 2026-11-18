import pandas as pd

df = pd.read_csv("logs.csv", encoding="utf-8")

df["gain"] = df["weight"] - df["weight"].iloc[0]
df["share"] = (df["kcal"] / df["kcal"].sum() * 100).round(1)

print(f"共 {len(df)} 条记录，{df.shape[1]} 列")
print(df.describe().round(2))

print(f"累计增重 {df['weight'].iloc[-1] - df['weight'].iloc[0]:.1f} kg")
print(f"总热量 {df['kcal'].sum()} kcal，平均每天 {df['kcal'].mean():.0f} kcal")

high = df[df["weight"] > df["weight"].mean()]
print(f"高于平均体重的 {len(high)} 天：")
print(high[["date", "weight", "kcal"]].to_string(index=False))

df.sort_values("weight", ascending=False).to_csv("result2.csv", index=False, encoding="utf-8")
print("已写入 result2.csv（按体重降序）")