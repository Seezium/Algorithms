arr = [-17,-45,-15,-33,-85,-56,-86,-30]
men = []
boys = []
for n in arr:
    if n%2 == 0:
        men.append(n)
    else:
        boys.append(n)

men.sort()
boys.sort(reverse= True)


print(men + boys)