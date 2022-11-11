#Problem 52
for a in range(10000,1000000):
    l1=[i for i in str(a)]
    l2=[i for i in str(2*a)]
    l3=[i for i in str(3*a)]
    l4=[i for i in str(4*a)]
    l5=[i for i in str(5*a)]
    l6=[i for i in str(6*a)]
    l1.sort()
    l2.sort()
    l3.sort()
    l4.sort()
    l5.sort()
    l6.sort()
    if (l1==l2) and (l1==l3) and (l1==l4) and (l1==l5) and (l1==l6):
        print(a)