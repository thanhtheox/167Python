import math

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
t = x
for i in range(1, n + 1, 1):
    t *= (x + i)
print("Tich la: ", t)

S = x
i = 1
while i <= n:
    S *= (x + i)
    i += 1

print("Gia tri cua S({},{}) la: {}".format(x, n, S))

