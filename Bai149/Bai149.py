a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
m = abs(a) 
n = abs(b) 
while (m * n != 0):
    if (m > n):
        m = m - n
    else:
        n = n - m
ucln = m + n
print("Uoc chung lon nhat cua ", a, " va ", b, " la: ", ucln)
