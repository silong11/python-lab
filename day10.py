import stats
from stats import average
import stats as st

records = stats.read_records("logs.txt")

if len(records) == 0:
    print("没有可用数据")
else:
    print(f"共 {len(records)} 条")
    print(f"平均体重 {stats.average(records):.2f} kg")
    print(f"最近三天 {st.average(records[-3:]):.2f} kg")
    h = stats.heaviest(records)
    print(f"最重 {h['date']} {h['weight']} kg")

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"共 {len(records)} 条记录\n")
        f.write(f"平均体重 {average(records):.2f} kg\n")
        f.write(f"最重 {h['date']} {h['weight']} kg\n")

print(f"stats 模块来自: {stats.__file__}")