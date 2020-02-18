def infected(s):
   
    totalcount = len(s)-s.count("X")
    
    s = s.split("X")
    totalinfected = 0
    for i in s:
        x = i.count("1")
        
        if x > 0:
            
            totalinfected += len(i)
    if totalinfected == 0:
        return 0
    else:

        return totalinfected/totalcount*100
  
    

    
print(infected("01000000X000X011X0X"))
print(infected("01X000X010X011XX"))
print(infected("XXXXX"))
print(infected("00000000X00X0000"))
print(infected("0000000010"))
print(infected("000001XXXX0010X1X00010"))
print(infected("X00X000000X10X0100"))