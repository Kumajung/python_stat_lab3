# โจทย์ข้อที่ 1 : โยนลูกเต๋า 2 ลูกพร้อมกัน ให้ตัวแปรสุ่ม X เป็นผลรวมของแต้มบนลูกเต๋า
import itertools
from collections import Counter
# 1. สร้างตัวอย่างทั้งหมดของการโยนลูกเต๋า 2 ลูก
# range(1, 7) ใช้จำลองค่าที่เป็นไปได้ของลูกเต๋าหนึ่งลูก 
#โดยเป็นช่วงตัวเลขตั้งแต่ 1 ถึง 6 ซึ่งครอบคลุมทุกหน้าของลูกเต๋ามาตรฐาน

outcomes = list(itertools.product(range(1, 7), repeat=2))  # ผลลัพธ์ทั้งหมด

# 2. คำนวณผลรวมของแต้มบนลูกเต๋า
sums = [sum(outcome) for outcome in outcomes]

# 3. นับจำนวนความถี่ของแต่ละผลรวม
frequency = Counter(sums)

# 4. คำนวณความน่าจะเป็นของแต่ละผลรวม
probability = {outcome: count / len(outcomes) for outcome, count in frequency.items()}

# แสดงผลลัพธ์   
# ใช้ for outcome ด้วย sorted(probability.items()



"""
Unit 3: Probability Distributions หน้า 52
 โจทย์ข้อที่ 2 
Crack Length (mm) for an Aluminum Alloy
data = [81, 98, 291, 101, 98, 118, 158, 197, 139, 249, 249, 135,
        223, 205, 80, 177, 82, 64, 137, 149, 117, 149,
        127, 115, 198, 342, 83, 34, 342, 185, 227, 225,
        185, 240, 161, 197, 98, 65, 144, 151, 134, 59,
        181, 151, 240, 146, 104, 100, 215, 200]
        
Probability Plots 2 แบบ
-เปรียบเทียบกับการแจกแจงปกติ
-เปรียบเทียบกับการแจกแจงปกติ LogNormal
"""
print()

