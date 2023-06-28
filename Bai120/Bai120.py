import math
n = int(input("Nhap n(n >= 2): "))
at = 2
i = 2
while(i <= n):
    ahh = 5 * at + math.sqrt(24 * at * at - 8)
    i = i + 1
    at = ahh
print("So hang thu n cua day: ", ahh)