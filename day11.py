class Record:
     def __init__(self, date, weight, kcal):
         self.date = date
         self.weight = weight
         self.kcal = kcal

     def summary(self):
         return f"{self.date}: {self.weight} kg, {self.kcal} kcal"

     def gain_since(self, other):
         return self.weight - other.weight

def read_records(path):
    records = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                try:
                    records.append(Record(parts[0], float(parts[1]), int(parts[2])))
                except (ValueError, IndexError):
                    print(f"跳过坏行：{line.strip()}")
    except FileNotFoundError:
        print(f"文件不存在：{path}")
    return records

def average(records):
        total = 0
        for r in records:
            total = total + r.weight
        return total / len(records)

records = read_records("logs.txt")

for r in records:
    print(r.summary())

print(f"共 {len(records)} 条记录")
print(f"平均体重 {average(records):.2f} kg")
print(f"从 {records[0].date} 到 {records[-1].date} 增重 {records[-1].gain_since(records[0]):.1f} kg")