x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
t = 1
for i in range(1, n + 1, 1):
    t = t * x
print("x^n: ", t)

x = float(input("Nhap co so x: "))
n = float(input("Nhap so mu n: "))
i = 1
while i <= n:
    t = x*x
    i += 1
print( x, " mu ", n, " = ", t)


