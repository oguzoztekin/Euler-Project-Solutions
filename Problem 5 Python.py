#Problem 5
import math
def smallestmultiple(n):
    t=1
    for i in range(1,n+1):
        t*=i//math.gcd(i,t)
    print(t)
smallestmultiple(20)

"""
#If you want to burn your computer, you can also use this code
for j in range(1,232792561):
    t=0
    for a in range(1,21):    
        if i%a==0:
            t+=1
    if t==20:
        print(i)
"""