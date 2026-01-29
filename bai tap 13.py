try:
    a = int(input("Nhập số nguyên thứ nhất (số bị chia): "))
    b = int(input("Nhập số nguyên thứ hai (số chia): "))
    result = a / b
    print(f"Kết quả: {a} / {b} = {result}")

except ZeroDivisionError:
    print("Lỗi: Không thể chia cho số 0!")
except ValueError:
    print("Lỗi: Dữ liệu nhập vào không phải là số nguyên hợp lệ!")
