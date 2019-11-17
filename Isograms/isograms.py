def is_isogram(string):
    
    x = list(string.upper())
    total = 0
    for i in x:
        total += x.count(i)
    if total > len(string):
        return False
    else:
        return True

print(is_isogram("Dermatoglyphics" ))
print(is_isogram("aba" )) 
print(is_isogram("moOse" )) 