try:
    age = int(input("Vui lòng nhập tuổi của bạn: "))
    if 1 <= age <= 120:
        print(f"Tuổi {age} là hợp lệ. Cảm ơn bạn!")
    else:
        print(f"Thông báo: Tuổi {age} không hợp lệ! Tuổi phải nằm trong khoảng từ 1 đến 120:")
except ValueError:
    print("Lỗi: Vui lòng nhập vào một số nguyên hợp lệ.")