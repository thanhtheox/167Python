import math

x = float(input("Nhap x: "))
n = int(input("Nhap n: "))

S = 0
i = 2
t = 1

while i <= 2*n:
    t = t * x * x
    S = S + t
    i += 2

print("Gia tri cua S({}, {}) la: {}".format(x, n, S))
