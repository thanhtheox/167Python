import math

n = float(input("Nhap n: "))
at = 2
i = 2

while i <= n:
    ahh = (-9*at - 24)/(5*at+13)
    i += 1
    at = ahh

print("So hang thu {} cua day so la: {}".format(n,ahh))


