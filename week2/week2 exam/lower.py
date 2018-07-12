import os
li ={'A':".-",'B':"-...",'C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':"--.",'H':"....",'I':"..",'J':".---",'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",
'P':".--.",'Q':"--.-",'R':".-.",'S':"...",'T': "-",'U':"..-",'V':"...-",'W':".--",'X':"-..-",'Y':"-.--",'Z':"--.."}
words =  ["hig", "sip", "pot"]      
pattr =[]

def pattern(w):
	st = ''
	w=w.upper()
	# print(w)
	for i in w:
		st=st+li.get(i)

	# print(st)
	return st



for w in words:

	s= pattern(w)
	# print(s)
	pattr.append(s)
unique = []
for i in pattr:
	if i not in unique:
		unique.append(i)
print(len(unique))