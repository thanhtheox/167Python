import math

x = float(input("Nhap x: "))
n = int(input("Nhap n: "))

S = 0
i = 1
t = 1

while i <= n:
    t = math.sin(x) * t
    s = s + t
    i += 1

print("Gia tri cua S({}, {}) la: {}".format(x, n, S))
