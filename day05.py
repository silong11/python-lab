# 今日练习内容：

weights = [67.0,67.4,67.9]
weights.insert(1,67.2)
print(weights)
weights.remove(67.4)
print(weights)
last = weights.pop()
print(weights,last)
weights[0] = 66.8
print(weights)
nums = [10,20,30,40,50,60]
print(nums[1:4])
print(nums[:3])
print(nums[3:])
print(nums[-2:])
print(nums[::-1])
print(nums[::2])
print(nums)
record = {"date": "10-25", "weight": 68.2, "kcal": 2700}
for k, v in record.items():
    print(k, "=", v)

record["meals"] = {"breakfast": 600, "lunch": 900, "dinner": 1200}
print(record["meals"])
print(record["meals"]["lunch"])

total_kcal = 0
for v in record["meals"].values():
    total_kcal = total_kcal + v
print(total_kcal)

# 今日交付内容：

records = [
    {"date": "10-21", "weight": 67.0, "kcal": 2500},
    {"date": "10-22", "weight": 67.4, "kcal": 2650},
    {"date": "10-24", "weight": 67.9, "kcal": 2800},
    {"date": "10-25", "weight": 68.2, "kcal": 2700},
]

for r in records:
    print(f"{r['date']} {r['weight']} kg {r['kcal']} kcal")

print("--- 最近两条 ---")
for r in records[-2:]:
    print(f"{r['date']} {r['weight']} kg {r['kcal']} kcal")
records.pop(1)

print(f"共 {len(records)} 条记录")

total = 0
for r in records:
    total = total + r["weight"]
print(f"平均体重 {total / len(records):.2f} kg")

heaviest = records[0]
for r in records:
    if r["weight"] > heaviest["weight"]:
        heaviest = r
print(f"最重: {heaviest['date']} {heaviest['weight']} kg")