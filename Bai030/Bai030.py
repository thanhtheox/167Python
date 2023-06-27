import math

n = int(input("Nhap n: "))
S = 0
i = 2
while i <= 2*n:
    S = S + 1/i
    i *= i
print("Tong S = ", S)
