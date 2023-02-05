import os
from pygame import mixer,init
from tkinter import *

init()

path = 'C:\\Users\\User\\Music'
index = 0
list1 = os.listdir(path)

mixer.music.load(list1[index])
text=list1[index]
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


root = Tk()
root.title("MUSICPLAYER")
root.geometry("270x300")
root.configure(bg="light yellow")


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

lbl = Label(root,text=f"playing: {text}",pady=10,font=("Arial",13))
lbl.place(relx=0.0,rely=0.6)
lbl.configure(bg="light yellow")

lbl2 = Label(root,text="HAVE FUN",pady=10,font=("Arial",30))
lbl2.place(relx=0.1,rely=0.3)
lbl2.configure(bg="light yellow")

root.mainloop()