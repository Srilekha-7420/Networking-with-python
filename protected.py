class class1:
    _p1 = "p1"
    p3 = "p3"
    __p4="p4"

class class2(class1):
    _p2 = "p2"

class class3(class2):

    print(class2._p2)
    print(class1._p1)
    print(class1.p3)
    print(class1.__p4)

from math import pi
pi()