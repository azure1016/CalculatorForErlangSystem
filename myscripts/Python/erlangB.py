# from math import sum
from decimal import Decimal

def jc(k):
    if k == 0:
        return 1
    if k < 0:
        return 1
    return k * jc(k - 1)


def erlB(s, a):
    mu = 0
    mu = Decimal(mu)
    for r in range(0, s + 1):
        mu = mu + Decimal(a ** r) / jc(r)

        #zi = long(a ** s) / long(jc(s))

    zi = Decimal(a ** s) / jc(s)
    Bl = Decimal(zi / mu)
    return Bl

s = Decimal(input())
a = Decimal(input())
print a-a*erlB(s,a)
print a*erlB(s,a)-a*erlB(s+2,a)
print a*erlB(s,a)




