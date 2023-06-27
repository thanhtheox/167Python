import math

n = float(input("Nhap n: "))
at = 1
bt = 1
i = 2

while i <= n:
    ahh = 3*bt + 2*at
    bhh = at + 3*bt
    i += 1
    at = ahh
    bt = bhh

print("So hang thu {} cua day so la: {}, {}".format(n,ahh, bhh))


