import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# สร้างข้อมูลสุ่มตามการแจกแจงปกติ
data = np.random.normal(loc=50, scale=10, size=25)

# สร้าง Q-Q plot
stats.probplot(data, plot=plt)
plt.title('Q-Q Plot')
plt.show()