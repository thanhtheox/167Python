from math import sqrt
xA = float(input("Nhap xA: "))
yA = float(input("Nhap yA: "))
xB = float(input("Nhap xB: "))
yB = float(input("Nhap yB: "))
xC = float(input("Nhap xC: "))
yC = float(input("Nhap yC: "))
a = sqrt((xB - xA) * (xB - xA) + (yB - yA) * (yB - yA))
b = sqrt((xC - xA) * (xC - xA) + (yC - yA) * (yC - yA))
c = sqrt((xC - xB) * (xC - xB) + (yC - yB) * (yC - yB))
if a + b > c and a + c > b and b + c > a:
    print("La tam giac")
else:
    print("Khong la tam giac")