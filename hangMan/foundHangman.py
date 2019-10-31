import turtle
import random

#Function used to build word from guesses
def get_guessed(word, guesses):
  out = ''
  for letter in word:
    if letter in guesses:
      out += letter
    else:
      out += '_'
  return out


# Create turtle and clear screen
screen = turtle.Screen()
t = turtle.Turtle()
screen.clear()

# Generate the word to guess
words = ["cat", "dog", "horse", "cow", "mouse"]
word = random.choice(words)

# Game Variables
game_over = False
guesses = []
errors = 0

# TODO #1: Set up drawing using Turtle: 
# ------
# |    |
# |
# |
# ------
val = turtle.Turtle() 
val.left(90)
val.forward(100)
val.right(90)
val.forward(50)
val.right(90)
val.forward(25)
val.penup()
val.forward(75)
val.right(90)
val.pendown()
val.forward(100)
val.backward(50)
val.right(90)
val.forward(100)
val.right(90)
val.forward(50)
val.right(90)
val.forward(25)

#Start the game loop
while not game_over:

  guess = input("Guess a letter: ")
  guesses += guess
  # TODO #2: Check for repeat guess/letter by user and print what letters has been guessed already (hint: using the 'guesses' list)
  print(guesses)
  
  if guess not in word:
    errors += 1
    # TODO #3: Draw next part of hangman using turtle (the stick figure)
    print (errors)
  if errors == 1:
    val.penup()
    val.right(90)
    val.forward(5)
    val.left(90)
    val.pendown()
    val.circle(5)
  if errors == 2:
    val.penup()
    val.left(90)
    val.forward(5)
    val.right(90)
    val.forward(5)
    val.pendown()
    val.forward(25)
    
    #Game losing conditions
    if errors == 6:
      print ("You lose!")
      print ("The word was " + word)
      game_over = True
 
  #Find out if letter is in randomly generated word
  guessed = get_guessed(word, guesses)
  print (guessed)
  
  # Game wining condition
  if guessed == word:
    print ("The word was " + word)
    print ("You win!")
    game_over = True
    