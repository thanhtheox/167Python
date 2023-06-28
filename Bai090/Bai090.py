x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
S = 0
t = 1
m = 1
i = 1
dau = -1
while i <= n:
    t = t * x
    m = m * i
    S += dau*t/m
    i += 1
    dau = -dau
print("Gia tri cua S({}, {}) la: {}".format(x, n, S))