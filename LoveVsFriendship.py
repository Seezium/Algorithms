def words_to_marks_mine(s):
    s = "attitude"
    letters = ('abcdefghijklmnopqrstuvwxyz')
    arr = []
    for n in s:
    
        x = letters.find(n)+1
        y = arr.append(x)
    print (sum(arr))

def words_to_marks(s):
    print (sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s))