#Problem 46
P=[]
Composite=[]
OC=[]
#Creating a list with primes
for i in range(2,10001):
    P.append(i)
    for j in range(2,5001):
        if i!=j:
            if (i%j==0):
                P.remove(i)    
                Composite.append(i)
                break
    
def test_goldbach(n):
    for p in P:
        for r in range(1,100): #100 is enough but also we can use p//2
            if n==p+2*(r**2):
                return True
def odd_composite():
    for a in Composite:
        if a%2==1:
            OC.append(a)
            if test_goldbach(a):
                OC.remove(a)
    return min(OC)
            
            
            
            
            
            
            
            
            
            



