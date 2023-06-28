n = int(input("Nhap n: "))
s = 0
m = 0
for i in range(1, n + 1, 1):
    m = m + i 
    s = s + 1/m
print("Tong la: ", s)