import math
try:
    num = float(input("Nhập một số: "))

    if num < 0:
        print("Lỗi: Không thể tính căn bậc hai của một số âm!")
    else:
        result = math.sqrt(num)
        print(f"Căn bậc hai của {num} là: {result:.2f}")
except ValueError:
    print("Lỗi: Vui lòng nhập một số hợp lệ!")