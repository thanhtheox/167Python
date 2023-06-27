from math import floor
n = float(input("Nhap n: "))
flag = 1
t = n
while (t >= 10):
    dv = t % 10 
    hc = floor(t/10) % 10
    if (hc > dv):
        flag = 0
    t = floor(t/10)
if (flag == 1):
    print("Tang")
else:
    print("Khong tang")