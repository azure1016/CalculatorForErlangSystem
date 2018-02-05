from decimal import Decimal


def jc(k):
    if k == 0:
        return 1
    return k * jc(k - 1)


def erlB(s, a):
    mu = 0
    mu = Decimal(mu)
    for r in range(1, s + 1):
        mu = mu + Decimal(a ** r) / jc(r)

        #zi = long(a ** s) / long(jc(s))
        zi = Decimal(a ** s) / jc(s)

        Bl = Decimal(zi / mu)
    return Bl

# if '__name__' == '__main__':
print "please enter s,a,rou"
s = input()
ar = input()

ar = Decimal(ar)
art = ar
rou = input()
rout = Decimal(rou)
number = ar + rout * art * erlB(s, art)
while abs(number - art) >= Decimal(0.001):
    art = number
    print number
    number = ar + rout * art * erlB(s, art)
else:
    print "the ar(total call) is " + str(art)
    print "B(s,ar) is" + str(erlB(s, art))
