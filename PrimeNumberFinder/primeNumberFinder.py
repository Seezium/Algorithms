#Prints the number of prime numbers between two numbers
start = 1
finish = 400
odds = []
arr = []
for k in range(start,finish):
    if k%2 != 0:
        odds.append(k)


for i in odds:
    x = 0
    for j in range(1,i):
        
        if i%j == 0:
            x += 1
    if x == 1:
        arr.append(i)
#print(arr)  #Print the array          
print(len(arr)) #Print the length of the array




