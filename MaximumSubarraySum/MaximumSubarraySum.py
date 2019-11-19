def maxSequence(arr):
  lowest = ans = total = 0
  for i in arr:
    total += i
    lowest = min(lowest, total)
    ans = max(ans, total - lowest)
  return ans

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))