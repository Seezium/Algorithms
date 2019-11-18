
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

print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(1168789))
print("--- %s seconds ---" % (time.time() - start_time))
