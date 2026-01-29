ten1 = input("Nhập tên SV 1: ")
toan1 = float(input("Điểm Toán SV 1: "))
ly1 = float(input("Điểm Lý SV 1: "))
hoa1 = float(input("Điểm Hóa SV 1: "))
dtb1 = (toan1 + ly1 + hoa1) / 3

ten2 = input("Nhập tên SV 2: ")
toan2 = float(input("Điểm Toán SV 2: "))
ly2 = float(input("Điểm Lý SV 2: "))
hoa2 = float(input("Điểm Hóa SV 2: "))
dtb2 = (toan2 + ly2 + hoa2) / 3

ten3 = input("Nhập tên SV 3: ")
toan3 = float(input("Điểm Toán SV 3: "))
ly3 = float(input("Điểm Lý SV 3: "))
hoa3 = float(input("Điểm Hóa SV 3: "))
dtb3 = (toan3 + ly3 + hoa3) / 3

print(ten1, "1", round(dtb1, 2))
print(ten2, "2", round(dtb2, 2))
print(ten3, "3", round(dtb3, 2))