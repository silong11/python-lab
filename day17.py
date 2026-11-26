import pandas as pd
import matplotlib.pyplot as plt
def load(path):
    df = pd.read_csv(path)
    print(f"读入{len(df)} 行， {df.shape[1]} 列")
    return df

if __name__ == "__main__":
    df = load("logs_dirty.csv")
    print(df.head())
def clean(df):
    df = df.drop_duplicates()
    df["weight"] = pd.to_numeric(
        df["weight"].str.replace("kg", "", regex=False),
        errors="coerce",
    )
    df = df.fillna({"weight": df["weight"].mean(), "kcal": df["kcal"].mean()})
    print(f"清洗后 {len(df)} 行，缺失 {df.isna().sum().sum()} 个")
    return df
def analyze(df):
    return {
        "条数": len(df),
        "平均体重": float(round(df["weight"].mean(), 2)),
        "最高体重": float(round(df["weight"].max(), 1)),
        "累计增重": float(round(df["weight"].iloc[-1] - df["weight"].iloc[0], 1)),
        "总热量": round(df["kcal"].sum()),
        "平均热量": round(df["kcal"].mean()),
    }

def plot(df, path):
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"] = False
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(df["date"], df["weight"], marker="o")
    axes[0].set_title("体重变化")
    axes[0].set_ylabel("kg")
    axes[1].bar(df["date"], df["kcal"], color="steelblue")
    axes[1].set_title("每日热量")
    axes[1].axhline(df["kcal"].mean(), color="red", linestyle="--", label="平均")
    axes[1].legend()
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    print(f"已保存 {path}")

if __name__ == "__main__":
    df = load("logs_dirty.csv")
    df = clean(df)
    plot(df, "report.png")
    print(analyze(df))
if __name__ == "__main__":
    df = load("logs_dirty.csv")
    df = clean(df)
    print(df)