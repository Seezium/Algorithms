'''
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
'''
import time
from itertools import permutations 
start_time = time.time()
def next_bigger(n):
    arr = []
    arr1 = []
    arr2 = []
    x = list(str(n))
    perm = permutations(x)
    x = ''.join(x)  
    
    for i in list(perm):
        x = ''.join(i) 
        arr.append(int(x))
    
    for j in arr:
        if j >= n:
            arr1.append(j)
        arr1.sort()

    if max(arr1) == n:
        return -1
    else:
        res = []
        for i in arr1: 
            if i not in res: 
                res.append(i)
        return res[1]




            
   
    
        
print(next_bigger(1168789))
print("--- %s seconds ---" % (time.time() - start_time))
#TODO: Turn numbers into a list


#TODO:List out all possible numbers in number
 
  
# Get all permutations of [1, 2, 3] 

  
# Print the obtained permutations 

#TODO: Find numbers greater than or equal to number

#TODO: Find the difference with the lowest number

#TODO: If they match then return -1