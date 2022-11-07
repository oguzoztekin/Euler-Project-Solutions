#Problem 30

l1=[]
toplam=0
for i in range(2,1000000):
    T=0
    a=i%10
    b=(i%100)-a
    c=(i%1000)-b-a
    d=(i%10000)-c-b-a
    e=(i%100000)-d-c-b-a
    f=(i%1000000)-e-d-c-b-a
    l=[a,b,c,d,e,f]
    liste=[int(a/10**l.index(a)) for a in l]
    for h in liste:
        T+=h**5
    if T==i:
        l1.append(i)
        toplam+=i

        
answer=[4150, 4151, 54748, 92727, 93084, 194979]

