def read_records(path):
    records = []
    try:
        with open(path, "r", encoding="utf-8")as f:
            for line in f:
                parts = line.strip().split(",")
                try:
                    r = {
                        "date": parts[0],
                        "weight":float(parts[1]),
                        "kcal": int(parts[2]),
                    }
                except(ValueError, IndexError):
                    print(f"跳过坏行：{line.strip()}")
                    continue
                records.append(r)
    except FileNotFoundError:
        print(f"文件不存在：{path}")
    return records

def average(rs):
    total = 0
    for i in rs:
        total = total +i["weight"]
    return total / len(rs)

def heaviest(rs):
    best = rs[0]
    for r in rs:
        if r["weight"] > best["weight"]:
            best = r
    return best

if __name__ == "__main__":
    print("stats.py  自测")
    rs = read_records("logs.txt")
    print(f"共 {len(rs)} 条，平均 {average(rs):.2f} kg")