def compare(m,n):
	count =0
	for i in range(len(m)):
		if(m[i]!=n[i]):
			count+=1
	print(count)
def binary(x,y):
	m="{0:b}".format(x)
	n="{0:b}".format(y)
	
	# n.type()
	for i in range(len(n)-len(m)):
		m='0'+m
	compare(m,n)
	

binary(1,4)
binary(25,30)
binary(100,250)
binary(1,30)
binary(0,255)
