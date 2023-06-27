import math

S = 4 - 2/4 - 1/5 - 1/6
t = 1
e = 1
i = 1

while e >= 10**(-6):
    t *= 16
    e = (4/(8*i+1) - (2/(8*i+4)) - 1/(8*i+5) - 1/(8*i+6)) / t
    S += e
    i += 1

print("Gia tri cua bieu thu la: {}".format(S))

