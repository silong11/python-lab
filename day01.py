# day01.py --肆龍的第一个python程序

weight = 67     #体重 kg
height = 176    #身高 cm
age = 19        #年龄

bmi = weight / (height /100) ** 2
bmr = 10 * weight + 6.25 * height - 5 * age + 5
tdee = bmr * 1.55

print("体重：", weight, "kg")
print("BMI:",round(bmi, 2))
print("基础代谢：",round(bmr), "kcal")
print("每日消耗：",round(tdee), "kcal")
print("增重目标：",round(tdee + 400), "kcal")
print("蛋白质目标：",round(weight * 1.8), "g")