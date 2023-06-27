import math

n = int(input("Nhap n: "))

S = 0
e = 0.5
i = 2

while e >= 10**(-6):
    e = 1/i
    S += e
    i += 2

print("Gia tri cua S({}) la: {}".format(n, S))


