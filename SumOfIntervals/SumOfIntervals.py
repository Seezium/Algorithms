def sum_of_intervals(intervals):
    arr = []
    res = []
    for n in intervals:
        for i in range(n[0], n[1]):
            arr = arr + [i]
            arr.sort()
    for n in arr:
        if n not in res:
            res.append(n)
    return len(res)

print(sum_of_intervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ))

print(sum_of_intervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ))

print(sum_of_intervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ))
