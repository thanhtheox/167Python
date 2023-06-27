import math

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

S = x
i = 1
while i <= n:
    S *= (x + i)
    i += 1

print("Gia tri cua S({},{}) la: {}".format(x, n, S))

