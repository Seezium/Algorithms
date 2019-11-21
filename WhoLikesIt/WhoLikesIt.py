def likes(names):
    if len(names) >= 4:
        length = len(names) - 2
        return "{}, {} and {} others like this".format(names[0],names[1],str(length))
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0],names[1],names[2])
    elif len(names) == 2:
        return "{} and {} like this".format(names[0],names[1])
    elif len(names) == 1:
        return "{} likes this".format(names[0])
    else:
        return "no one likes this"

print(likes([]), 'no one likes this')
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))