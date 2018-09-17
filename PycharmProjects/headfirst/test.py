import pickle
import sys
import objgraph
from itertools import *

def var_print():
    info = "info inside"
    print(info)

info = "info outside"
var_print()
print(info)

print("dir list")
#nothing happened!
#print(dir(list))
print("help list")
#help(list)
#help()
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

# for i in gen():
#     print(str(i)+"\n")

#help(pickle.load)

a = [1]
b=a
a=b
del a
del b
#objgraph.show_refs([a],filename="ref_a.png")
#objgraph.show_refs([b],filename="ref_b.png")
#objgraph.show_refs([c],filename="ref_c.png")
print(sys.getrefcount('q!#werty'))
print(sys.getrefcount([1]))
#print(sys.getrefcount(c))
d ={k:v for k,v in enumerate("Vamei") if v not in "mi"}
#print(d)

result = list(takewhile(lambda x: x<5,[1,3,6,4]))
print(result)

def heigh_class(h):
    if h>180:
        return "tall"
    elif h<160:
        return "short"
    else:
        return "middle"

friends = [191,158,159,165,170,177,181,182,190]
friends =  sorted(friends,key = heigh_class)
print(friends)
for m,n in groupby(friends,key=heigh_class):
    print(m)
    print(sorted(list(n)))