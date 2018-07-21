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
		else:
			count=0 
		y = y // 2
	if(temp<=1):
		return 0
	else:
		return temp
print(func(0))
print(func(55))
print(func(-5))
print(func(12354))
print(func(6))
print(func(256))