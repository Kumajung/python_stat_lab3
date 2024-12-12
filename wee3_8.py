"""
Unit 3: Probability Distributions หน้า 40-41
กิจกรรม 5
การหาพื้นที่ภายใต้ตาราง Z สมมติว่าค่า Z = 1 
งานของเราคือค้นหาพื้นที่แรเงานั้น (พื้นที่เหนือค่า Z ตั้งแต่ 0 ถึง 1) 
    1. อ่านคอลัมน์แรกของตาราง Z จนกว่าคุณจะพบแถวที่ขึ้นต้นด้วย 1.0 
    2. จากนั้นอ่านแถวแรกและค้นหาคอลัมน์ที่ขึ้นต้นด้วย 0.0 (หมายความว่า Z = 1.0) 
    3. อ่านค่าในเซลล์ที่อยู่จุดตัดของแถว 1.0 และคอลัมน์ 0.0 นี่คือ 0.3413 เท่ากับ 34.13%
    การหาพื้นที่ใต้ตาราง Z ดังนั้น ความน่าจะเป็นที่ 0 ≤ Z ≤ 1 คือ 34.13% 
    P(0 ≤ Z ≤ 1 ) = 0.3413 = 34.13% 
        1. ถ้า Z = 1.65 ความน่าจะเป็น = ? 
        2. ถ้า Z = -1.65 ความน่าจะเป็น = ?
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# คำนวณพื้นที่ใต้กราฟ Z-table
z1 = 1.65
z2 = -1.65

# ความน่าจะเป็นที่ 0 <= Z <= z1
p_0_to_z1 = norm.cdf(z1) - norm.cdf(0)

# ความน่าจะเป็นที่ 0 <= Z <= |z2| (สมมาตรของการแจกแจงแบบปกติ)
p_0_to_z2 = norm.cdf(0) - norm.cdf(z2)

# สร้างข้อมูลสำหรับกราฟ
x = np.linspace(-3, 3, 1000)
y = norm.pdf(x)

# สร้างกราฟ
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Standard Normal Distribution", color="blue")

# แรเงาพื้นที่ 0 <= Z <= 1.65
x_fill_z1 = np.linspace(0, z1, 500)
y_fill_z1 = norm.pdf(x_fill_z1)
plt.fill_between(x_fill_z1, y_fill_z1, color="green", alpha=0.5, label="P(0 ≤ Z ≤ 1.65)")

# แรเงาพื้นที่ -1.65 <= Z <= 0
x_fill_z2 = np.linspace(z2, 0, 500)
y_fill_z2 = norm.pdf(x_fill_z2)
plt.fill_between(x_fill_z2, y_fill_z2, color="orange", alpha=0.5, label="P(-1.65 ≤ Z ≤ 0)")

# เพิ่มรายละเอียดในกราฟ
plt.title("Standard Normal Distribution and Shaded Areas")
plt.xlabel("Z-values")
plt.ylabel("Probability Density")
plt.axvline(0, color="black", linestyle="--", linewidth=1)
plt.axvline(z1, color="green", linestyle="--", linewidth=1, label="Z = 1.65")
plt.axvline(z2, color="orange", linestyle="--", linewidth=1, label="Z = -1.65")
plt.legend()
plt.grid()

# แสดงผลลัพธ์
plt.show()
print("ความน่าจะเป็นที่ 0 ≤ Z ≤ 1.65: {:.4f} ({:.2f}%)".format(p_0_to_z1, p_0_to_z1 * 100))
print("ความน่าจะเป็นที่ -1.65 ≤ Z ≤ 0: {:.4f} ({:.2f}%)".format(p_0_to_z2, p_0_to_z2 * 100))

# - norm.cdf: ใช้ในการคำนวณฟังก์ชันสะสม (Cumulative Distribution Function) ของการแจกแจงปกติ
# - p_0_to_z1: คำนวณพื้นที่ใต้กราฟจาก Z = 0 ถึง Z = 1.65
# - p_0_to_z2: คำนวณพื้นที่ใต้กราฟจาก Z = -1.65 ถึง Z = 0
# - ใช้ matplotlib เพื่อสร้างกราฟ และแรเงาพื้นที่ที่สนใจ

