from tkinter import *
from PIL import ImageTk, Image
import random
import sys

#game data
wordList = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop", "laptop", "dog", "cat", "lemon", "cable", "mirror", "hat", "apple", "cricket", "football", "chalk", "blackboard", "buzz", "scorpion", "engineering", "channel", "sports", "tiger", "sun", "moon", "jupiter", "saturn", "google", "zeus", "asus", "banana", "lemon", "sky", "night", "india", "australia", "england", "parris", "germany", "london"]
lives = 10
score = 0
image_paths=['hang.jpg','nineth.png','eighth.png','seventh.png','sixth.png','fifth.png','fourth.png','third.png','second.png','first.png','zero.jpg']

#window creation
win = Tk()
win.title("Hangman GUI")

#game initialize function
def initialize():
	global secretword
	secretword = random.choice(wordList) #returns random word to secret word
	wordlength = len(secretword)
	#print(secretword)
	global guessword
	guessword = []
	for character in secretword:
		guessword.append("*")
	#window components
	global hintLabel
	hintLabel=Label(win, text="Lenth of word is "+ str(wordlength) )
	hintLabel.grid(column=0, row=0)
	global livesLabel
	livesLabel=Label(win, text="Remaining lives "+ str(lives) )
	livesLabel.grid(column=0, row=1)
	global wordShow
	wordShow=Label(win, text=guessword)
	wordShow.grid(column=0, row=2)
	global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26
	btn1 = Button(win, text="q",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("q"))
	btn1.grid(column=1, row=3)
	btn2 = Button(win, text="w",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("w"))
	btn2.grid(column=2, row=3)
	btn3 = Button(win, text="e",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("e"))
	btn3.grid(column=3, row=3)
	btn4 = Button(win, text="r",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("r"))
	btn4.grid(column=4, row=3)
	btn5 = Button(win, text="t",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("t"))
	btn5.grid(column=5, row=3)
	btn6 = Button(win, text="y",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("y"))
	btn6.grid(column=6, row=3)
	btn7 = Button(win, text="u",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("u"))
	btn7.grid(column=7, row=3)
	btn8 = Button(win, text="i",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("i"))
	btn8.grid(column=8, row=3)
	btn9 = Button(win, text="o",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("o"))
	btn9.grid(column=9, row=3)
	btn10 = Button(win, text="p",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("p"))
	btn10.grid(column=10, row=3)
	btn11 = Button(win, text="a",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("a"))
	btn11.grid(column=1, row=4)
	btn12 = Button(win, text="s",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("s"))
	btn12.grid(column=2, row=4)
	btn13 = Button(win, text="d",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("d"))
	btn13.grid(column=3, row=4)
	btn14 = Button(win, text="f",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("f"))
	btn14.grid(column=4, row=4)
	btn15 = Button(win, text="g",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("g"))
	btn15.grid(column=5, row=4)
	btn16 = Button(win, text="h",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("h"))
	btn16.grid(column=6, row=4)
	btn17 = Button(win, text="j",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("j"))
	btn17.grid(column=7, row=4)
	btn18 = Button(win, text="k",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("k"))
	btn18.grid(column=8, row=4)
	btn19 = Button(win, text="l",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("l"))
	btn19.grid(column=9, row=4)
	btn20 = Button(win, text="z",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("z"))
	btn20.grid(column=1, row=5)
	btn21 = Button(win, text="x",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("x"))
	btn21.grid(column=2, row=5)
	btn22 = Button(win, text="c",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("c"))
	btn22.grid(column=3, row=5)
	btn23 = Button(win, text="v",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("v"))
	btn23.grid(column=4, row=5)
	btn24 = Button(win, text="b",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("b"))
	btn24.grid(column=5, row=5)
	btn25 = Button(win, text="n",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("n"))
	btn25.grid(column=6, row=5)
	btn26 = Button(win, text="m",bg="Yellow", fg="Black",width=1,height=1,command=lambda: gameUpdate("m"))
	btn26.grid(column=7, row=5)
	global statusLabel
	statusLabel=Label(win, text="Game in Progress....")
	statusLabel.grid(column=0, row=6)
	global img
	img = Image.open(image_paths[lives])
	img = img.resize((200, 200), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	global panel
	panel = Label(win, image = img)
	panel.grid(column=0, row=7)

#update function
def gameUpdate(guess):
	global lives
	global secretword
	if guess in secretword:
		array = list(secretword)
		for x in range( 0,len(secretword) ):
			if str( array[x] ) == guess:
				guessword[x] = str(guess)
		wordShow.configure(text=guessword)
		if not '*' in guessword:
			gameWin()
	else:
		lives = lives-1
		image = Image.open(image_paths[lives])
		image = image.resize( (200, 200), Image.ANTIALIAS )
		img = ImageTk.PhotoImage(image)
		panel.configure(image=img)
		panel.image = img
		if lives == 0:
			gameLoss()
		livesLabel.configure(text="\tRemaining lives "+ str(lives) )
		wordShow.configure(text=guessword)

#disable function
def gameDisable():
	btn1.configure(state='disabled')
	btn2.configure(state='disabled')
	btn3.configure(state='disabled')
	btn4.configure(state='disabled')
	btn5.configure(state='disabled')
	btn6.configure(state='disabled')
	btn7.configure(state='disabled')
	btn8.configure(state='disabled')
	btn9.configure(state='disabled')
	btn10.configure(state='disabled')
	btn11.configure(state='disabled')
	btn12.configure(state='disabled')
	btn13.configure(state='disabled')
	btn14.configure(state='disabled')
	btn15.configure(state='disabled')
	btn16.configure(state='disabled')
	btn17.configure(state='disabled')
	btn18.configure(state='disabled')
	btn19.configure(state='disabled')
	btn20.configure(state='disabled')
	btn21.configure(state='disabled')
	btn22.configure(state='disabled')
	btn23.configure(state='disabled')
	btn24.configure(state='disabled')
	btn25.configure(state='disabled')
	btn26.configure(state='disabled')

#game restart function
def gameDestroy():
	
	btn1.destroy()
	btn2.destroy()
	btn3.destroy()
	btn4.destroy()
	btn5.destroy()
	btn6.destroy()
	btn7.destroy()
	btn8.destroy()
	btn9.destroy()
	btn10.destroy()
	btn11.destroy()
	btn12.destroy()
	btn13.destroy()
	btn14.destroy()
	btn15.destroy()
	btn16.destroy()
	btn17.destroy()
	btn18.destroy()
	btn19.destroy()
	btn20.destroy()
	btn21.destroy()
	btn22.destroy()
	btn23.destroy()
	btn24.destroy()
	btn25.destroy()
	btn26.destroy()
	hintLabel.destroy()
	livesLabel.destroy()
	wordShow.destroy()
	statusLabel.destroy()
	#img.destroy()
	panel.destroy()
	btnContinue.destroy()

#win function
def gameWin():
	global score
	score = score + 1
	statusLabel.configure(text="You won!!!!\nYour Score is " + str(score) )
	gameDisable()
	global btnContinue
	btnContinue = Button(win, text="Next Game",command=lambda: gameNext() )
	btnContinue.grid(column=0, row=8)

#lose function
def gameLoss():
	statusLabel.configure(text="You Lose????\nYour Score is " + str(score) + "\nActual word was "+ secretword)
	gameDisable()
	global btnContinue
	btnContinue = Button(win, text="Restart",command=lambda: gameRestart() )
	btnContinue.grid(column=0, row=8)

#game menu
def gameNext():
	gameDestroy()
	global lives
	lives = 10
	initialize()

#game Restart
def gameRestart():
	gameDestroy()
	global score
	score = 0
	global lives
	lives = 10
	initialize()

#win main-loop
initialize()
win.mainloop()