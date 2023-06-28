from math import sqrt
n = float(input("Nhap n: "))
s = 0
i = n
while(i > 0):
    s = sqrt(i + s)
    i = i - 1
print("S = ", s)