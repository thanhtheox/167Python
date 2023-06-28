import math
n = int(input("Nhap n: "))
S = 0
t = 1
i = 1
while i <= n:
    t = t * i
    S = math.sqrt(t + S)
    i += 1
print("Gia tri cua S({}) la: {}".format(n, S)) 