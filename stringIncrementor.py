def increment_string(string):
    
    head = string.rstrip('0123456789')
    
    if len(string) == len(head):
        
        string = "{}{}".format(head,"1")
    else:
        length = len(string)-len(head)
        tail = string[len(head):]
        tail = int(tail) + 1
        tail = '{0:0{width}}'.format(tail, width=(len(string)-len(head)))
        newString = (str(head),str(tail))
        
        final = "{}{}".format(head, tail)
    
    return final

print(increment_string("foo23"))

