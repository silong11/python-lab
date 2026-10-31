line = "10-25,68.2,2700"
parts = line.split(",")
print(parts)
print(len(parts))

text = "10-25, 68.2 , 2700"
cleaned = []
for p in text.split(","):
    cleaned.append(p.strip())
print(cleaned)

print(",".join(cleaned))
print("-".join(cleaned))

print(text.replace("2700", "2800"))
print(text)

log = """10-21,67.0,2500
10-22,67.4,2650
10-24,67.9,2800
10-25,68.2,2700"""

records = []
for line in log.strip().split("\n"):
    parts = line.split(",")
    r = {"date": parts[0], "weight": float(parts[1]), "kcal": int(parts[2])}
    records.append(r)

print(f"共解析出 {len(records)}条记录")
print(records[0])
def average(rs):
    total = 0
    for r in rs:
        total = total + r["weight"]
    return total / len(rs)
def heaviest(rs):
    best = rs[0]
    for r in rs:
        if r["weight"] > best["weight"]:
            best = r
    return best

print(f"平均体重 {average(records):.2f} kg")
print(f"最近三天平均 {average(records[-3:]):.2f} kg")
h = heaviest(records)
print(f"最重 {h['date']} {h['weight']} kg")