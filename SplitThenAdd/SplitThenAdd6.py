def split_and_add(numbers, n):
    for i in range(n):
        if len(numbers) % 2 == 0:

            x =len(numbers)//2
            firstArr = numbers[0:x]
            secArr = numbers[x:len(numbers)]
            numbers = []
            for i in range(len(firstArr)):
                numbers.append(firstArr[i]+secArr[i])
            
              
        else:
            x =len(numbers)//2
            firstArr = numbers[0:x]
            firstArr.insert(0,0)
            secArr = numbers[x:len(numbers)]
            numbers = []
            for i in range(len(firstArr)):
                numbers.append(firstArr[i]+secArr[i])
              
    return numbers

print(split_and_add([4, 2, 5, 3, 2, 5, 7], 2))
print(split_and_add([1,2,3,4,5], 2))
print(split_and_add([1,2,3,4,5], 3))
print(split_and_add([15], 3))
print(split_and_add([32,45,43,23,54,23,54,34], 2))
print(split_and_add([32,45,43,23,54,23,54,34], 0))
print(split_and_add([3,234,25,345,45,34,234,235,345], 3))
print(split_and_add([3,234,25,345,45,34,234,235,345,34,534,45,645,645,645,4656,45,3], 4))
print(split_and_add([23,345,345,345,34536,567,568,6,34536,54,7546,456], 20))