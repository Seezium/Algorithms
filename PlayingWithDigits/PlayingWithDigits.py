def dig_pow(n, p):
    m = n
    n = list(str(n))
    arr = []
    
    for i in n:
        x = int(i)**p
        p +=1
        arr.append(x)
    if sum(arr) % m == 0:
        return sum(arr)/m
    else:
        return -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))