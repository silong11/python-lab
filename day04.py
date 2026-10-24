weights = [67.0,67.4,67.9]
print(weights)
print(len(weights))
print(weights[0])
print(weights[-1])
weights.append(68.3)
print(weights)
record = {"date":"10-24","weight":68.3,"kcal":2600}
print(record)
print(record["weight"])
print(len(record))
record["kcal"] = 2800
record["note"] = "腿"
print(record)
for k in record:
    print(k,record[k])

records = []

records.append({"date":"10-21","weight":67.0,"kcal":2500})
records.append({"date":"10-22","weight":67.4,"kcal":2650})
records.append({"date":"10-24","weight":67.9,"kcal":2800})

for r in records:
    print(r["date"],r["weight"])

total = 0
for r in records:
    total = total+r["weight"]

avg = total / len((records))
print(f"平均体重{avg:.2f}kg")
print(f"最新一条:{records[-1]['date']},{records[-1]['weight']}kg")

records.append({"date":10-25, "weight":68.2, "kcal":2700})

print(f"共{len(records)}条记录")
print(f"累计增重{records[-1]['weight'] - records[0]['weight']:.1f} kg")