n = int(input("Nhap n: "))
tich = 1
t = n
while(t != 0):
    dv = int(t % 10)
    tich = tich * dv
    t = int(t / 10)
print("Tich cac chu so cua n: ", tich)