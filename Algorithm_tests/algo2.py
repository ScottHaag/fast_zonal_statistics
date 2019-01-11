import numpy as np;
import math;

def algo2(u,v):
    C = [];
    
    if u[0] > v[0]:
        v,u = u,v

    c1 = math.floor(u[0] + .4999999)
    c2 = math.floor(v[0] - .4999999)
       
    if c1 > c2:
        return C
    
    deltax = v[0] - u[0]
    deltay = v[1] - u[1]
    
    for x in range(int(c1),int(c2+1),1):
        ##print( (((( x + 0.5 - u[0] ) / (deltax)) * (deltay)) + u[1]  ) )
        y = int(math.floor(((( x + 0.5 - u[0] ) / (deltax)) * (deltay)) + u[1] - 0.4999 ))
        ##print(y)
        C.append([x,y])
    return C

u = [1.25,10]
v = [1.49,100]

print algo2([1.25,10],[1.49,100])
print algo2([1.49,10],[1.56,100])
print algo2([1.51,9.5],[3.5,9.5])
print algo2([3.5,9.5],[1.51,9.5])

print algo2([1.49,9.5],[3.5,9.5])
print algo2([3.5,9.5],[1.49,9.5])


print algo2([1.49,9.4],[3.5,9.4])
print algo2([3.5,9.4],[1.49,9.4])

print algo2([1.49,9.4],[3.5,5.5])
print algo2([3.5,5.5],[1.49,9.4])