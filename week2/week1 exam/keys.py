# Example: [[1], [0,2], [3]] – true                
#  [[1,3], [3,0,1], [2], [0]] – false 
#  Test case1: [[1], [0,2], [3]] – true
#  Test case2: [[1,3], [3,0,1], [2], [0]] – false 
#  Test case3: [[1,2,3], [0], [0], [0]] – true 
# Test case4: [[1], [0,2,4], [1,3,4], [2], [1,2]] – true 
# Test case5: [[1], [2,3], [1,2], [4], [1], [5]] – false 
# Test case6: [[1], [2], [3], [4], [2]] – true 
# Test case7: [[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]] – false
def key(lis):
	yes =[]
	for i in range(len(lis)):
		yes.append('no entry')
	yes[0]='entry'
	for i in range(len(lis)):
		for j in range(len(lis[i])):


			if(i==0 and yes[i]=='no entry' or yes[i]=='entry' and lis[i][j]<len(lis)):


				yes[lis[i][j]]='entry'
	count = 0
	print(yes)
	for i in range(len(yes)):
		if(yes[i] == 'no entry'):
			print("False")
			count = 0
			break
		else:
			count+=1
	if(count!=0):
		print("True")




key([[1], [0,2], [3]])
key([[1,3], [3,0,1], [2],[0]])
key([[1,2,3], [0], [0],[0]])
key([[1], [0,2,4], [1,3,4], [2], [1,2]])
key([[1], [2,3], [1,2], [4], [1], [5]])
key([[1], [2], [3], [4], [2]])
key([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])