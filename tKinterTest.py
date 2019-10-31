from tkinter import *
import os
os.system('clear')



root = Tk()
root.title('Codemy.com - Learn to Code!')
root.geometry("400x600")

def hello():
    hello_label = Label(root, text="Hello " + myTextbox.get())
    hello_label.pack()

myLabel = Label(root, text="Enter your first name:")
myLabel.pack() #Puts in first spot, grid() you specify where to place it


myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit", command=hello)
myButton.pack()






root.mainloop()