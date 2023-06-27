x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
t = 1
m = 1
dau = -1
for i in range(1, n + 1, 1):
    t = t * x
    m = m * i
    s=s+dau*t/m 
    dau = - dau
print("Tong la: ", s)











