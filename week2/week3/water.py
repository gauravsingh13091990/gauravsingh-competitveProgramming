
 
def Water(l, n):
 
    
    lef = [0]*n
 
    
    
    rig = [0]*n
 
    
    wat = 0
 
    
    lef[0] = l[0]
    for i in range( 1, n):
        lef[i] = max(lef[i-1], l[i])
 
    
    rig[n-1] = l[n-1]
    for i in range(n-2, -1, -1):
        rig[i] = max(rig[i+1], l[i]);
 
  
    for i in range(0, n):
        wat += min(lef[i],rig[i]) - l[i]
 
    return wat
 
 
# Driver program
 
l1 = [0, 5, 1, 3, 4, 0, 1]
l2=	[0, 1, 0, 2, 1, 0, 1]
l3=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
l4=[0, 1, 0, 2, 1, 0, 5, 1, 0, 2]
l5=[0, 1, 0, 5, 1, 0, 2]
n1= len(l1)
n2=len(l2)
n3=len(l3)
n4=len(l4)
n5=len(l5)
print(Water(l1, n1))
print(Water(l2, n2))
print(Water(l3, n3))
print(Water(l4, n4))
print(Water(l5, n5))
