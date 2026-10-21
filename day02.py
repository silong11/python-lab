# 交互式热量计算器

name   = input("你的名字:")
weight = float(input("你的体重(kg):"))
height = float(input("身高(cm):"))
age    = int(input("年龄:"))

bmi  = weight / (height / 100) ** 2
bmr  = 10 * weight + 6.25 * height - 5 * age + 5
tdee = bmr *1.55

print()
print(f"{name},你的数据:")
print(f" BMI         : {bmi:.2f}")
print(f" 基础代谢     : {bmr:.0f} kcal")
print(f" 每日消耗     : {tdee:.0f} kcal")
print(f" 增重目标     : {tdee + 400:.0f} kcal")
print(f" 蛋白质       : {weight *1.8:.0f} g ")

if bmi < 18.5:
    print(f"结论：偏瘦，还差 {75 - weight:.1f} kg 到目标")
elif bmi <24:
    print(f"结论：正常范围，还差 {75 - weight:.1f} kg 到目标")
else:
    print("结论：偏重，注意体脂。")