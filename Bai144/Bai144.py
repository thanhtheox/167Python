n = float(input("Nhap n: "))
dem = 0 
i = 1
while(i <= n):
    if(n % i == 0):
        dem = dem + 1
    i = i + 1
if(dem == 2):
    print("n La so nguyen to")
else:
    print("n Khong la so nguyen to")
