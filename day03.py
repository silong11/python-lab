bmi = 26

if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
else:
    print("偏重")


total = 0
for i in range(1, 101):
    total = total + i

print("1 加到 101 =", total)


weight = 67.0
week = 0

while weight < 75:
    weight = weight + 0.35
    week = week + 1

print(f"从 67kg 增到 75kg，需要 {week} 周")