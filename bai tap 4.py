def sum_two_numbers(a, b):
    """Hàm này nhận vào hai số nguyên và trả về tổng của chúng"""
    return a + b
z1=int(input("Nhập số thứ nhất: "))
z2= int(input("Nhập số thứ hai: "))
ket_qua = sum_two_numbers(z1, z2)
print(f"Kết quả của phép tính {z1} + {z2} là: {ket_qua}")