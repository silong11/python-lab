def read_records(path):
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            records.append({
                "date": parts[0],
                "weight": float(parts[1]),
                "kcal": int(parts[2]),
            })
    return records

def average(rs):
    total = 0
    for r in rs:
        total = total +r["weight"]
    return total / len(rs)

def heaviest(rs):
    best = rs[0]
    for r in rs:
        if r["weight"] > best["weight"]:
            best = r
    return best

records = read_records("logs.txt")
print(f"共 {len(records)} 条记录")
print(f"平均体重 {average(records):.2f} kg")
print(f"最近三天平均 {average(records[-3:]):.2f}")
h = heaviest(records)
print(f"最重 {h['date']} {h['weight']} kg")

with open("result.txt", "w", encoding="utf-8")as f:
    f.write(f"平均体重 {average(records):.2f} kg\n")
    f.write(f"最重 {h['date']} {h['weight']} kg\n")