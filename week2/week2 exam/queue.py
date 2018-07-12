class li(object):
    
    def re(self, p):
        
        def func(ppeople):
            return -ppeople[0],ppeople[1]
        p.sort(key=func)
        for i in range(len(p)):

            if i>=len(p):

                break
            if(p[i][1]==i):

                continue

            temp=p[i]

            p.pop(i)

            p.insert(temp[1],temp)
        return p

ob = li()
p1 = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
p2 = [[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]
p3 = [[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]
print(ob.re(p1))
print(ob.re(p2))
print(ob.re(p3))

