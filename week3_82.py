"""
Unit 3: Probability Distributions หน้า 40-41
กิจกรรม 6
1. ความน่าจะเป็นเท่าใดที่นักช้อปรายใดที่สุ่มเลือกใช้จ่ายมากกว่า 80 ปอนด์ต่อสัปดาห์? 
2. % ของนักช้อปที่มีแนวโน้มจะใช้จ่ายระหว่าง 30 ถึง 80 ปอนด์ต่อสัปดาห์คือเท่าไร? 
3. ระดับค่าใช้จ่ายที่เกิน 10% ของลูกค้าคืออะไร?
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# กำหนดพารามิเตอร์ของการแจกแจงปกติ
mean = 50  # ค่าเฉลี่ย (ค่าใช้จ่ายเฉลี่ยต่อสัปดาห์ในปอนด์)
std_dev = 15  # ส่วนเบี่ยงเบนมาตรฐาน (ปอนด์)

# 1. ความน่าจะเป็นที่ลูกค้าใช้จ่ายมากกว่า £80
threshold_80 = 80
p_more_than_80 = 1 - norm.cdf(threshold_80, loc=mean, scale=std_dev)

# 2. เปอร์เซ็นต์ของลูกค้าที่ใช้จ่ายระหว่าง £30 ถึง £80
lower_30 = 30
upper_80 = 80
p_between_30_and_80 = norm.cdf(upper_80, loc=mean, scale=std_dev) - norm.cdf(lower_30, loc=mean, scale=std_dev)

# 3. ระดับการใช้จ่ายที่เกินกว่า 10% ของลูกค้า
p_exceed_10_percent = 0.9  # 90% ด้านล่าง หมายความว่าอีก 10% ด้านบน
expenditure_10_percent = norm.ppf(p_exceed_10_percent, loc=mean, scale=std_dev)

# แสดงผลลัพธ์
print("1. ความน่าจะเป็นที่ลูกค้าใช้จ่ายมากกว่า £80: {:.4f}".format(p_more_than_80))
print("2. เปอร์เซ็นต์ของลูกค้าที่ใช้จ่ายระหว่าง £30 ถึง £80: {:.2f}%".format(p_between_30_and_80 * 100))
print("3. ระดับการใช้จ่ายที่เกินกว่า 10% ของลูกค้า: £{:.2f}".format(expenditure_10_percent))

# สร้างกราฟแสดงการแจกแจง
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
y = norm.pdf(x, loc=mean, scale=std_dev)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Normal Distribution", color="blue")

# แรเงาพื้นที่ที่ Z > 80
x_fill_80 = np.linspace(threshold_80, mean + 4 * std_dev, 500)
y_fill_80 = norm.pdf(x_fill_80, loc=mean, scale=std_dev)
plt.fill_between(x_fill_80, y_fill_80, color="red", alpha=0.5, label="P(> £80)")

# แรเงาพื้นที่ที่ 30 <= Z <= 80
x_fill_30_80 = np.linspace(lower_30, upper_80, 500)
y_fill_30_80 = norm.pdf(x_fill_30_80, loc=mean, scale=std_dev)
plt.fill_between(x_fill_30_80, y_fill_30_80, color="green", alpha=0.5, label="P(£30 ≤ Z ≤ £80)")

# เพิ่มรายละเอียดในกราฟ
plt.title("Expenditure Distribution")
plt.xlabel("Expenditure (£)")
plt.ylabel("Probability Density")
plt.axvline(threshold_80, color="red", linestyle="--", label="£80 Threshold")
plt.axvline(lower_30, color="green", linestyle="--", label="£30 Threshold")
plt.axvline(upper_80, color="green", linestyle="--", label="£80 Threshold")
plt.axvline(expenditure_10_percent, color="orange", linestyle="--", label="Top 10% Expenditure")
plt.legend()
plt.grid()

# แสดงกราฟ
plt.show()

# - mean และ std_dev: ใช้กำหนดการแจกแจงปกติของค่าใช้จ่าย
# - norm.cdf: ใช้คำนวณความน่าจะเป็นสะสมสำหรับการแจกแจงปกติ
# - norm.ppf: ใช้หาเปอร์เซ็นไทล์สำหรับการแจกแจงปกติ
# - p_more_than_80: ความน่าจะเป็นที่ใช้จ่ายมากกว่า £80
# - p_between_30_and_80: ความน่าจะเป็นที่ใช้จ่ายอยู่ในช่วง £30 ถึง £80
# - expenditure_10_percent: ระดับค่าใช้จ่ายที่เกิน 10% ของลูกค้า
