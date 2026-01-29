def is_even(n):
    """Tra ve true neu chia het cho 2,nguoc lai tra ve false"""
    if n/2 == 0:
        return True
    else:
        return False
so_lieu = int(input("Nhập một số nguyên: "))

if is_even(so_lieu):
 print(f"{so_lieu} là số chẵn.")
else:
 print(f"{so_lieu} là số lẻ.")