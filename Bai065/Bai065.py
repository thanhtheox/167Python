n = float(input("Nhap n: "))
lc = n%10
t = abs(n)
while (t != 0):
    dv = t % 10
    if(dv < lc):
        lc = dv
    t = t//10
print("Chu so nho nhat cua so nguyen duong la: ", lc)