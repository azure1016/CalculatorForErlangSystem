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
    mu = 0
    mu = Decimal(mu)
    for r in range(0, s + 1):
        mu = mu + Decimal(a ** r) / jc(r)

        #zi = long(a ** s) / long(jc(s))

    zi = Decimal(a ** s) / jc(s)

    Bl = Decimal(zi / mu)
    return Bl


def rapp():

    print "please enter s1,a1,s2,a2,s3,a3"
    
    s1 = Decimal(input())
    a1 = Decimal(input())
    s2 = Decimal(input())
    a2 = Decimal(input())
    s3 = Decimal(input())
    a3 = Decimal(input())
 
    if math.ceil(a1) > 0 and math.ceil(s1) > 0:
        alfa1 = a1 * erlB(s1, a1)
    else:
        alfa1 = Decimal(0)
    print "alfa1 = " + str(alfa1)

    if Decimal(a2) > 0 and s2 > 0:
        alfa2 = a2 * erlB(s2, a2)
    else:
        alfa2 = Decimal(0)
    print "alfa2 = " + str(alfa2)

    if Decimal(a3) > 0 and s3 > 0:
        alfa3 = a3 * erlB(s3, a3)
    else:
        alfa3 = Decimal(0)
    print "alfa3 = " + str(alfa3)
    
    alfa = alfa1 + alfa2 + alfa3
    print "alfa = alfa1 + alfa2 + alfa3 = "+str(alfa)
    vofl1 = alfa1 * (1 - alfa1 + a1 / (1 + s1 + alfa1 - a1))
    print "vofl1 = "+str(vofl1)
    vofl2 = alfa2 * (1 - alfa2 + a2 / (1 + s2 + alfa2 - a2))
    print "vofl2 = " + str(vofl2)
    vofl3 = alfa3 * (1 - alfa3 + a3 / (1 + s3 + alfa3 - a3))
    print "vofl3 = " + str(vofl3)
    v = vofl1 + vofl2 + vofl3
    print "v = vofl1 + vofl2 + vofl3 =" +str(v)
    z = v / alfa
    print "z=v/alfa = "+str(z)
    print "please enter c ="
 #   c = input()
    a = v + 3 * z * (z - 1)
    print "a = v + 3 * z * (z - 1) = "+str(a)
    s = a * (alfa + z) / (alfa + z - 1) - alfa - 1
    print " s = a * (alfa + z) / (alfa + z - 1) - alfa - 1 = "+str(s)
    s_ = math.floor(s)
    s_ = Decimal(s_)
    print "equaled 's' is :" + str(s_)
    a = (s_ + alfa + 1) * (alfa + z - 1) / (alfa + z)
    print "equaled 'a' is :" + str(a)
    alfa_e = a * erlB(s, a)
    ap = a - alfa_e
    v = ap * (1 - a * (erlB(s - 1, a) - erlB(s, a)))
    z = v / ap
    '''
    print "equal system's passed call:aB(s+c,a)=" + str(a - a * erlB(s_ + c, a))
    print "B(s+c,a)=" + str(erlB(s_ + c, a))
    print "refused call :aB(s+c,a)=" + str(a * erlB(s_ + c, a))
    print "equaled var is" + str(v)
    print "mount factor is" + str(z)
'''
print rapp()
