#def mystery_range(s,n):
    #TODO: Break apart list
	#TODO: try first number 
    #TODO:if difference from first and second number is 
    
#print(mystery_range('6291211413114538107',14))

string = '6291211413114538107'
for n in range(0,9):
    if n in string:
        number = string.count(n)
        string.replace(n,'')
        print("{}:{}".format(n, number))



