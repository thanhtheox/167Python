import math

x = float(input("Nhap x: "))

S = 1
t = 1
m = 1
i = 1
e = 1
i = 1

while e >= 10**(-6):
    t *= x
    m *= i
    e = t / m
    S += e
    i += 1

print("Gia tri cua S({}) la: {}".format(x, S))
