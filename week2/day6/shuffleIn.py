import random

def shuffle(the_list):
    # Shuffle the input in place

    for j in range(len(the_list)):
        
        i= random.randint(0, len(the_list) - 1)
        
        the_list[j], the_list[i] = the_list[i  ], the_list[j]


sample_list = [1, 2, 3, 4, 5]
print(
'Sample list:', sample_list)


print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)