import math

xA, yA = map(float, input("Nhap toa do diem A (xA yA): ").split())
xB, yB = map(float, input("Nhap toa do diem B (xB yB): ").split())
xC, yC = map(float, input("Nhap toa do diem C (xC yC): ").split())

xM, yM = map(float, input("Nhap toa do diem M (xM yM): ").split())


SABC = 0.5 * abs(xA*(yB-yC) + xB*(yC-yA) + xC*(yA-yB))

SABM = 0.5 * abs(xA*(yB-yM) + xB*(yM-yA) + xM*(yA-yB))
SACM = 0.5 * abs(xA*(yM-yC) + xM*(yC-yA) + xC*(yA-yM))
SBCM = 0.5 * abs(xB*(yM-yC) + xM*(yC-yB) + xC*(yB-yM))

if SABM + SACM + SBCM == SABC:
    print("Diem M nam trong ABC")
else:
    print("Diem M khong nam trong ABC")

