from decimal import Decimal


def jc(k):
    if k == 0:
        return 1
    return k * jc(k - 1)


def erlB(s, a):
    mu = 0
    mu = Decimal(mu)
    #c = input()
    for r in range(1, s + 1):
        mu = mu + Decimal(a ** r) / jc(r)

        #zi = long(a ** s) / long(jc(s))
        zi = Decimal(a ** s) / jc(s)

        Bl = Decimal(zi / mu)
    return Bl

# if '__name__' == '__main__':
print "please enter initial s,a and B(s,a) needed"
s = input()
a = input()
tgt_B = input ()
a = Decimal(a)
c = 0
while abs(erlB(s,a) - Decimal(tgt_B) )>= Decimal(0.005):
    #art = number
    s = s+1
    c = c+1
else:
    print "the ideal c = " + str(c)
    print "the ideal s = " + str(s)
    print "B(s,a) is" + str(erlB(s, a))
