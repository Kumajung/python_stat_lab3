import pandas as pd  # นำเข้าไลบรารี pandas เพื่อใช้งานการวิเคราะห์ข้อมูล

# กำหนดอายุเป็นลิสต์
ages = [17, 18, 18, 18, 18, 19, 20, 20, 21]

# ใช้ pandas สร้าง Series
ages_series = pd.Series(ages)

# เรียกใช้ฟังก์ชัน describe() เพื่อหาสถิติพื้นฐาน
print("สถิติพื้นฐาน:")
print(ages_series.describe().round(2))

# คำนวณสถิติเพิ่มเติม
median = ages_series.median()
data_range = ages_series.max() - ages_series.min()
mode = ages_series.mode()[0]

print("_______________________________")
print(f"Median: {median}")
print(f"Range: {data_range}")
print(f"Mode: {mode}")