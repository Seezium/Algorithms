def find_outlier(integers):
    arr = []
    for i in integers:
        x = i%2
        y = arr.append(x)

    if sum(arr) > 1:
        for j in integers:
            if j % 2 == 0:
                answer = j
    else:
        for j in integers:
            if j % 2 != 0:
                answer = j

    return answer

print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))