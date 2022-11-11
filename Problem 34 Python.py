#Problem 34
def factorial(s):
    t=1
    if s==0:
        t*=1
    else:
        for a in range(1,s+1):
            t*=a
    return(t)
def problem34(a):
    s=0
    for i in range(3,a+1):
        l=[a for a in str(i)]
        l1=[int(b) for b in l]
        t=0
        for c in l1:
            t+=factorial(c)
        if i==t:
            s+=i
    print(s)
problem34(100000)