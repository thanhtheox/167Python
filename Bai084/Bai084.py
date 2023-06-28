import math
x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
t = x
for i in range(1, n + 1, 1):
    t = math.sin(t)
    s = s + t
print("Tong la: ", s)