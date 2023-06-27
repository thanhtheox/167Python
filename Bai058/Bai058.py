import math

n = int(input("Nhap so nguyen duong n: "))
t = n
s = 0
while t > 0:
    dv = t % 10
    s += dv
    t //= 10
print("Tong cac chu so cua", n, "la:", s)
