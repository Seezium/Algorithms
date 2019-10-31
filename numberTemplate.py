template = "+555 aaaa bbbb"
numbers = "18031978"
count = 0
#If template is char replace with 
for n in template:
    if template[n].isalpha():
        n.replace(n, numbers[count])
        count += 1
print(template)
    