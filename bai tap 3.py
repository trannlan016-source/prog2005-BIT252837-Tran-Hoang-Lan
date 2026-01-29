a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
tong = a + b
hieu = a - b
tich = a * b
if b != 0:
    thuong = a / b
else:
    thuong = "Không thể chia cho 0"
print(f"Tổng: {a} + {b} = {tong}")
print(f"Hiệu: {a} - {b} = {hieu}")
print(f"Tích: {a} * {b} = {tich}")
print(f"Thương: {a} / {b} = {thuong}")