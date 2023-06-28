x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 1
t = 1
for i in range(1, n + 1, 1):
    t = t * x
    s = s + t
print("Tong la: ", s)