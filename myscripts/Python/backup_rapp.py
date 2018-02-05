from decimal import Decimal
import math
import sys
sys.setrecursionlimit(1500)


def jc(k):
    if k == 0:
        return 1
    if k < 0:
        return 1
    return k * jc(k - 1)


def erlB(s, a):
    mu = 1
    mu = Decimal(mu)
    for r in range(1, s + 1):
        mu = mu + Decimal(a ** r) / jc(r)

        #zi = long(a ** s) / long(jc(s))
    zi = Decimal(a ** s) / jc(s)

    Bl = Decimal(zi / mu)
    return Bl


def rapp():
    print "please enter s,a"
    s = input()
    a = input()
    #s = Decimal(s)
    a = Decimal(a)
    alfa = a * erlB(s, a)
    ap = a - alfa
    v = ap * (1 - a * (erlB(s - 1, a) - erlB(s, a)))
    z = v / ap
    vofl = alfa * (1 - alfa + a / (1 + s + alfa - a))
    print "first router's --passed-- call :ap = a-aB(s,a) = " + str(ap)
    print "--refused-- call is :aB(s,a) = " + str(alfa)

    print "first router's var = " + str(v)
    print "mount factor of first router's --passed call-- z= :" + str(z)
    print
    print "call --arrived-- at backup router is alfa = " + str(alfa)
    print "backup router's var of --overflow-- call is vofl=:" + str(vofl)
    print "z =" + str(vofl / alfa)
        #print "neglect...."
    a = v + 3 * z * (z - 1)

    s = a * (alfa + z) / (alfa + z - 1) - alfa - 1
    s_ = math.floor(s)
    s_ = Decimal(s_)
    print "equaled 's' is :" + str(s_)
    a = (s_ + alfa + 1) * (alfa + z - 1) / (alfa + z)
    print "equaled 'a' is :" + str(a)
    alfa = a * erlB(s, a)
    ap = a - alfa
    v = ap * (1 - a * (erlB(s - 1, a) - erlB(s, a)))
    z = v / ap
    #v = alfa * (1 - alfa + a / (s + 1 + alfa - a))
    #z = v / alfa
# print erlB(s,a)
    print "backup router's passed call:" + str(a - a * erlB(s_, a))
    print "refused call" + str(a * erlB(s_, a))
    print "equaled var is" + str(v)
    print "mount factor is" + str(z)

print rapp()
