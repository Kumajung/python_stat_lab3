"""
Unit 3: Probability Distributions หน้า 22
กิจกรรมที่ 1: ข้อใดต่อไปนี้เป็นฟังก์ชันความน่าจะเป็น 
a. f(x)= 0.25 สําหรับ x = 9,10,11,12 
b. f(x)= (3-x)/2 สําหรับ x = 1,2,3,4 
c. f(x)= (x2+x+1)/25 สําหรับ x = 0,1,2,3
"""
def is_probability_function(f, x_values):
  """
  ตรวจสอบว่าฟังก์ชัน f เป็นฟังก์ชันความน่าจะเป็นหรือไม่

  Args:
    f: ฟังก์ชันความน่าจะเป็น
    x_values: ค่าของตัวแปรสุ่ม

  Returns:
    True ถ้า f เป็นฟังก์ชันความน่าจะเป็น
    False ถ้า f ไม่เป็นฟังก์ชันความน่าจะเป็น
  """

  probabilities = [f(x) for x in x_values]

  # ตรวจสอบว่าค่าความน่าจะเป็นทั้งหมดอยู่ระหว่าง 0 ถึง 1
  if not all(0 <= p <= 1 for p in probabilities):
    return False

  # ตรวจสอบว่าผลรวมของความน่าจะเป็นทั้งหมดเท่ากับ 1
  if sum(probabilities) != 1:
    return False

  return True

# กำหนดฟังก์ชันที่ต้องการตรวจสอบ
def f1(x):
  return 0.25

def f2(x):
  return (3-x)/2

def f3(x):
  return (x**2 + x + 1)/25

# กำหนดค่าของตัวแปรสุ่ม
x_values_1 = [9, 10, 11, 12]
x_values_2 = [1, 2, 3, 4]
x_values_3 = [0,1,2,3]

# ตรวจสอบฟังก์ชัน
print(is_probability_function(f1, x_values_1))  # Output: True
print(is_probability_function(f2, x_values_2))  # Output: False
print(is_probability_function(f3, x_values_3))  # Output: False