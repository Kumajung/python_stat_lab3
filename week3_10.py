import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# ตัวอย่างข้อมูลที่ป้อนด้วย array
data = np.array([10, 12, 15, 9, 14, 11, 13, 10, 15, 12])

# สร้าง Normal Probability Plot
plt.figure(figsize=(8, 6))
stats.probplot(data, dist="norm", plot=plt)

# แสดงกราฟ
plt.title('Normal Probability Plot')
plt.show()