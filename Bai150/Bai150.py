a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
m = abs(a)
n = abs(b)
while(m * n != 0):
    if(m > n):
        m = m - n
    else:
        n = n - m
bcnn = int(abs(a * b) / (m + n))
print("Boi chung nho nhat cua a va b la: ", bcnn)