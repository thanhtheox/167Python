from math import floor
n = float(input("Nhap n: "))
dem = 0
t = abs(n)
while (t != 0):
    dem = dem + 1
    t = floor(t/10)
print("So luong chu so cua so nguyen duong ", n, "la: ",dem)