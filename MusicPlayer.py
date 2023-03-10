# importing all needed libraries
import os
from pygame import mixer,init
from tkinter import *

# initialising ygame
init()

# som important variables
path = 'C:\\Users\\User\\Music'
index = 0
list1 = os.listdir(path)

mixer.music.load(list1[index])
text=list1[index]

# buttons command functions

def play():
	mixer.music.play()

def pause():
	mixer.music.pause()

def unpause():
	mixer.music.unpause()

def forward(index):
	if index != 0:
		index -= 1
	mixer.music.load(list1[index])
	text=list1[index]
	lbl = Label(root,text=f"playing: {text}",pady=10,padx=10,font=("Arial",13))
	lbl.place(relx=0.0,rely=0.6)
	lbl.configure(bg="light yellow")

def backward(index):
	if index != len(list1)+1:
		index += 1
	mixer.music.load(list1[index])
	text=list1[index]
	lbl = Label(root,text=f"playing: {text}",pady=10,padx=10,font=("Arial",13))
	lbl.place(relx=0.0,rely=0.6)
	lbl.configure(bg="light yellow")

# creating the window
root = Tk()
root.title("MUSICPLAYER")
root.geometry("270x300")
root.configure(bg="light yellow")

# creating and placing all buttons
playbtn = Button(root, text="PLAY",padx=10,pady=15,command=play)
playbtn.place(relx=0.0,rely=0.8)
playbtn.configure(bg="gold")

pausebtn = Button(root, text="PAUSE",padx=7,pady=15,command=pause)
pausebtn.place(relx=0.2,rely=0.8)
pausebtn.configure(bg="red")

resumebtn = Button(root, text="RESUME",padx=5,pady=15,command=unpause)
resumebtn.place(relx=0.4,rely=0.8)
resumebtn.configure(bg="light blue")

fbtn = Button(root, text="<",padx=10,pady=15,command=lambda : forward(index))
fbtn.place(relx=0.65,rely=0.8)
fbtn.configure(bg="grey")

bbtn = Button(root, text=">",padx=10,pady=15,command=lambda : backward(index))
bbtn.place(relx=0.8,rely=0.8)
bbtn.configure(bg="grey")

# creating the labels
lbl = Label(root,text=f"playing: {text}",pady=10,font=("Arial",13))
lbl.place(relx=0.0,rely=0.6)
lbl.configure(bg="light yellow")

lbl2 = Label(root,text="HAVE FUN",pady=10,font=("Arial",30))
lbl2.place(relx=0.1,rely=0.3)
lbl2.configure(bg="light yellow")


# this if statement ensures that our program will execute only when our file is runned directly not by importing it
if __name__=="__main__":
# running the loop
	root.mainloop()
