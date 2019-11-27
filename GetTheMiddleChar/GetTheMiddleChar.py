def get_middle(s):
    x = len(s)//2
    if len(s) % 2 == 0:
        
        return "{}{}".format(s[x-1],s[x])
    else:
        return s[x]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))

