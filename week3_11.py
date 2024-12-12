import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# ตัวอย่างข้อมูล
crack_lengths = np.array([0.5, 1.2, 1.8, 2.1, 2.4, 2.9, 3.5, 4.2, 5.0, 6.7])

# คำนวณค่า log ของข้อมูล (Log-transformation)
log_crack_lengths = np.log(crack_lengths)

# สร้าง Lognormal Probability Plot
stats.probplot(log_crack_lengths, dist="norm", plot=plt)

# เพิ่มชื่อกราฟ
plt.title("Lognormal Probability Plot for Crack-Length Data")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Ordered Values (Log-Transformed)")
plt.grid(True)
plt.show()
