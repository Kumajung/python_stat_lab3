"""
Unit 3: Probability Distributions หน้า 33
กิจกรรม 4 
วิธีแก้ไข ให้ X แสดงกระแสเป็นมิลลิแอมแปร์ ความน่าจะเป็นที่ร้องขอสามารถแสดงเป็น P(X>13) 
ความน่าจะเป็นนี้แสดงเป็นพื้นที่แรเงาภายใต้ฟังก์ชันความหนาแน่นของความน่าจะเป็นปกติในรูปนี้ 
น่าเสียดายที่ไม่มีนิพจน์แบบปิดสําหรับอินทิกรัลของฟังก์ชันความหนาแน่นของความน่าจะเป็นปกติ 
และความน่าจะเป็นตามการแจกแจงแบบปกติมักจะพบเป็นตัวเลขหรือจากตาราง
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# กำหนดพารามิเตอร์ของการแจกแจงแบบปกติ
mean = 10  # ค่าเฉลี่ย (มิลลิแอมแปร์)
variance = 4  # ความแปรปรวน (มิลลิแอมแปร์²)
std_dev = np.sqrt(variance)  # ส่วนเบี่ยงเบนมาตรฐาน

# คำนวณความน่าจะเป็น P(X > 13)
threshold = 13
p_greater_than_13 = 1 - norm.cdf(threshold, loc=mean, scale=std_dev)

# สร้างข้อมูลสำหรับกราฟ
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
y = norm.pdf(x, loc=mean, scale=std_dev)

# สร้างกราฟ
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Normal Distribution", color="#6495ED")

# แรเงาพื้นที่ P(X > 13)
x_fill = np.linspace(threshold, mean + 4 * std_dev, 1000)
y_fill = norm.pdf(x_fill, loc=mean, scale=std_dev)
plt.fill_between(x_fill, y_fill, color="#6495ED", alpha=0.5, label="P(X > 13)")

# เพิ่มรายละเอียดในกราฟ
plt.title("Normal Distribution: Mean=10, Variance=4")
plt.xlabel("Current (mA)")
plt.ylabel("Probability Density")
plt.axvline(x=threshold, color="black", linestyle="--", label="Threshold (X=13)")
plt.legend()
plt.grid()

# แสดงผลลัพธ์
plt.show()
print("ความน่าจะเป็นที่กระแสเกิน 13 มิลลิแอมแปร์: {:.4f}".format(p_greater_than_13))

# - mean: ค่าเฉลี่ยของการแจกแจงแบบปกติ (10 มิลลิแอมแปร์)
# - variance: ความแปรปรวน (4 มิลลิแอมแปร์²), std_dev: ส่วนเบี่ยงเบนมาตรฐาน (รากที่สองของความแปรปรวน)
# - norm.cdf: ใช้คำนวณค่าความน่าจะเป็นสะสมของการแจกแจงแบบปกติ
# - p_greater_than_13: ความน่าจะเป็นที่ X > 13 คำนวณจาก 1 - CDF(13)
# - สร้างกราฟแสดงฟังก์ชันความหนาแน่น และแรเงาพื้นที่ที่ X > 13 เพื่อแสดงภาพชัดเจน
