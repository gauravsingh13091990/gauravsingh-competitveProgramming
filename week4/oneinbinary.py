def func(y):

	a=0
	count=0
	temp=0
	while(y > 0):
		a = y % 2
		if(a == 1):
			count = count + 1
			if(temp<count):
				temp=count
		y = y // 2
	return temp
i = 15
j=16
k=1
l=25
m=5
n=6
li=[]
lj=[]
lk=[]
ll=[]
lm=[]
ln=[]
for i in range(i+1):
	t = func(i)
	li.append(t)
print(li)
for j in range(j+1):
	a = func(j)
	lj.append(a)
print(lj)
for k in range(k+1):
	a = func(k)
	lk.append(a)
print(lk)
for l in range(l+1):
	a = func(l)
	ll.append(a)
print(ll)
for m in range(m+1):
	a = func(m)
	lm.append(a)
print(lm)
for n in range(n+1):
	a = func(n)
	ln.append(a)
print(ln)

# print(func(0))
# print(func(55))
# print(func(-5))
# print(func(12354))
# print(func(6))
# print(func(256))