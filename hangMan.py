from playsound import playsound

#Simple Hangman game
print("\n"*15)
word = input('What is the secret word?')  
word = word.upper() 
listWord = list(word)    
print("\n"*15)
boardLength = len(word)
print(" "*boardLength)
board = "_"*boardLength
listBoard = list(board)
print(listBoard)
print(" "*boardLength)

arr = []
letterGuess = []
health = 10
#while health >0:
while listWord != listBoard and health != 0:   
    

    guess = input('Guess a letter: ')
    guess = guess.upper()
    if guess in letterGuess:
        print("Letter Already Chosen")
    else:

        for n in range(0,boardLength):
            if word[n] == guess:
                listBoard[n] = guess.upper()
        if guess not in word:
            health -= 1
        letterGuess.append(guess)
        letterGuess.sort()
        print("\n"*20)
        print(listBoard)
        print("\n")
        print("Your current health is: {}".format(health)) 
        print("\n")  
        print("Letters Chosen: {}".format(letterGuess))    
        print("\n"*5)
if listWord == listBoard and health != 0:
    print("You Win! Your score is: {}".format(health))
    playsound('/path/to/a/sound/file/you/want/to/play.mp3')
else:
    print("You Lose!")
    playsound('/path/to/a/sound/file/you/want/to/play.mp3')
