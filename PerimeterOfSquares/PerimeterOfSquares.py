def perimeter(n):
    
    arr = [1,1]
    for i in range(2,n+1):
        total = arr[i-1]+arr[i-2]
        arr.append(total)
    return sum(arr*4)

print(perimeter(5))
print(perimeter(7))
print(perimeter(20))
print(perimeter(30))
print(perimeter(100))