# s = input("Enter input for s")

# t = input("Enter input for t")
# Test case1: anagram, nagaram – true 
# Test case2: Keep, Peek – true 
# Test case3: Mother In Law, Hitler Woman – true 
# Test case4: School Master, The Classroom – true 
# Test case5: ASTRONOMERS, NO MORE STARS – true 
# Test case6: Toss, Shot – false 
# Test case7: joy, enjoy – false 
# Test case8: Debit Card, Bad Credit – true 
# Test case9: SiLeNt CAT, LisTen AcT – true 
# Test case10: Dormitory, Dirty Room – true 
s= 'Debit Card'
t = 'Bad Credit'
def fun(s,t):
	if(len(s)!=len(t)):
		return False

	for i in t:
		count =0
		if i  not in s:
			return False

			
	return True
s1 =s.replace(" ","").lower()
t1= t.replace(" ","").lower()
print(fun(s1,t1))			



