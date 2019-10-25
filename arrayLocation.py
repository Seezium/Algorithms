#Example arrays of coordinates
a = input("What array do you want (1-6)? : ")

if a == "1":
    arr = [[1,3,5],[2,0,10],[-3,1,4],[4,2,4],[1,1,5],[-3,0,12],[2,1,12],[-2,2,6]]
elif a == "2":
    arr = [[4,0,8],[2,1,2],[1,0,5],[-3,3,16],[2,2,2],[-1,1,7],[0,0,5],[-4,3,14]]
elif a == "3":
    arr = [[1,1,20],[1,2,30],[1,3,8],[1,0,2],[1,1,6],[1,2,4],[1,3,6],[-7,0,100]]
elif a == "4":
    arr = [[2,2,100],[3,1,25],[4,0,8],[-6,3,25],[-1,2,80],[8,0,12],[-10,3,220],[0,1,150]]
elif a == "5":
    arr = [[3,2,80],[1,1,25],[6,0,8],[-5,3,50],[1,2,100],[4,0,9],[-8,3,260],[0,1,90]]
elif a == "6":
    arr = [[4,0,8],[2,1,2],[1,0,5],[-3,3,16],[2,2,2],[-1,1,7],[0,0,5],[-4,3,14]]
else:
    print("Please enter a valid number (1-6)!")
    exit()
#Start position
startPos = [0,0]
startArr = [0,0,0]
layer = 0
for n in arr:
    layer = layer+n[0]
    if n[1] == 0: #North
        startPos = [startPos[0],startPos[1]+(n[2]*(2**layer))]
    elif n[1] == 1: #East
        startPos = [startPos[0]+(n[2]*(2**layer)),startPos[1]]
    elif n[1] == 2: #South
        startPos = [startPos[0],startPos[1]-(n[2]*(2**layer))]
    elif n[1] == 3: #West
        startPos = [startPos[0]-(n[2]*(2**layer)),startPos[1]]
print(startPos)        
    
