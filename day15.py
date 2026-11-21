import pandas as pd

df = pd.read_csv("logs_dirty.csv")
before = len(df)
df = df.drop_duplicates()
print(f"去重：{before} → {len(df)} 行")

df["weight"] = pd.to_numeric(df["weight"].str.replace("kg", "", regex=False), errors="coerce")

print(f"缺失单元格：{df.isna().sum().sum()} 个")
print(df[df.isna().any(axis=1)])

df = df.fillna({"weight": df["weight"].mean(), "kcal": df["kcal"].mean()})
print(f"填补后缺失：{df.isna().sum().sum()} 个")

df["dt"] = pd.to_datetime("2026-" + df["date"], format="%Y-%m-%d")
df["week"] = df["dt"].dt.isocalendar().week

weekly = df.groupby("week")[["weight", "kcal"]].mean().round(2)
print(weekly)

print(f"总计 {len(df)} 条，平均体重 {df['weight'].mean():.2f} kg，最高 {df['weight'].max():.1f} kg")

weekly.to_csv("result3.csv", encoding="utf-8")
print("已写入 result3.csv")