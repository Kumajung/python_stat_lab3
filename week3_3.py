# ตัวอย่างที่ไม่ต่อเนื่อง: โยนเหรียญ 3 เหรียญ โยนเหรียญ 3 เหรียญพร้อมกัน ให้ตัวแปรสุ่ม X เป็นจํานวนหัวที่แสดง

from itertools import product

# สร้างผลลัพธ์ที่เป็นไปได้ทั้งหมดของการโยนเหรียญ 3 เหรียญ
outcomes = list(product(['H', 'T'], repeat=3))

# กำหนดตัวแปรสุ่ม X เป็นจำนวนหัว (Heads) ในแต่ละผลลัพธ์
head_counts = [outcome.count('H') for outcome in outcomes]

# คำนวณความน่าจะเป็นของแต่ละจำนวนหัว
probabilities = {}
for count in range(4):  # จำนวนหัวสามารถเป็น 0, 1, 2, หรือ 3
    probabilities[count] = head_counts.count(count) / len(outcomes)

# แสดงผลลัพธ์
print("ผลลัพธ์การโยนเหรียญ (Outcomes):")
print(outcomes)
print("\nความน่าจะเป็นของจำนวนหัว (Probabilities):")
for head_count, prob in probabilities.items():
    print(f"จำนวนหัว {head_count}: {prob:.2f}")

# แสดงข้อมูลด้วยคอมเม้นภาษาไทย
# - ใช้ itertools.product เพื่อสร้างผลลัพธ์ทุกแบบของการโยนเหรียญ (H = หัว, T = ก้อย)
# - นับจำนวน 'H' ในแต่ละผลลัพธ์ และบันทึกใน list head_counts
# - คำนวณความน่าจะเป็นโดยนับจำนวนผลลัพธ์ที่มีจำนวนหัวแต่ละแบบ แล้วหารด้วยจำนวนผลลัพธ์ทั้งหมด
# - แสดงผลลัพธ์ในรูปแบบที่เข้าใจง่าย