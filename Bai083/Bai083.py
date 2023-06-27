import math
x = float(input("Nhap x: "))
n = float(input("Nhap n: "))
s = 0
t = 1
i = 1
while (i <= n):
    t = t * x
    s = s + math.sin(t)
    i = i + 1
print("S = ", s)