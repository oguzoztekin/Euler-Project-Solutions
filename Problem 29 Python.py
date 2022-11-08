#Problem 29
l=[]
for i in range(2,101):
    for j in range(2,101):
        a=i**j
        if not(a in l):
            l.append(a)
print(len(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    