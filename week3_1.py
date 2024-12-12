import pandas as pd

# ข้อมูลอายุและความถี่
ages = [17, 18, 19, 20, 21]
frequencies = [1, 4, 1, 2, 1]

# ขยายข้อมูลตามความถี่
data = []
for age, freq in zip(ages, frequencies):
    data.extend([age] * freq)

# สร้าง DataFrame
df = pd.DataFrame(data, columns=["Age"])

# ใช้ describe() เพื่อหาค่าสถิติพื้นฐาน
stats = df["Age"].describe()

# แสดงผล
print(stats)