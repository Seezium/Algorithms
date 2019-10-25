'''
Takes a user inputed card number
Prints a hidden key so number is not fully visible
'''
cc = input("Enter your credit card number :")
dd = cc[-4:]
x =len(cc)-4
cc = "{}{}".format(x*"#",dd)
print(cc)

    


