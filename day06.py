records = [
    {"date": "10-21", "weight": 67.0, "kcal": 2500},
    {"date": "10-22", "weight": 67.4, "kcal": 2650},
    {"date": "10-24", "weight": 67.9, "kcal": 2800},
    {"date": "10-25", "weight": 68.2, "kcal": 2700},
]

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
print(f"全部平均 {average(records):.2f} kg")
print(f"最近三天平均 {average(records[-3:]):.2f} kg")

h = heaviest(records)
print(f"最重 {h['date']} {h['weight']} kg")