import math

n = int(input("Nhap so nguyen duong n: "))

t = n
lc = n % 10
while t != 0:
    dv = t % 10
    if dv > lc:
        lc = dv
    t //= 10

print("Chu so lon nhat cua", n, "la:", lc)

