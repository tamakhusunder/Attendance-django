###Gui for face recognition server

from tkinter import *
from tkinter import filedialog
import os

window=Tk()
window.iconbitmap(r'.\icons\logo1.ico')
window.title('Face Recognition')
window.geometry('800x400')

#function for running server and for capturing photo 
def server():
	os.system('python app.py')
    
def camera():
    os.system('python camera_feed.py')

###display text and image and button
l0=Label(window,text='Welcome to face recognition system for running servers')
l0.config(font=("Courier", 20,"bold"))
l0.pack(pady=10)

middleframe=Frame(window)
middleframe.pack(pady=20)

pic1=PhotoImage(file='.\icons\chip.png')
# but1=Button(middleframe,image=pic1,command=capture)
but1=Label(middleframe,image=pic1)
but1.grid(column=0,row=0,padx=25)
b1=Button(middleframe,text='Server',command=server,bg='black',fg='white')
b1.config(font=("Courier", 10,"bold"))
b1.grid(column=0,row=1,padx=20,pady=20)


pic3=PhotoImage(file='./icons/camera.png')
# but3=Button(middleframe,image=pic3,command=recognize)
but3=Label(middleframe,image=pic3)
but3.grid(column=2,row=0,padx=25)
b3=Button(middleframe,text='Camera',command=camera,bg='black',fg='white')
b3.config(font=("Courier", 10,"bold"))
b3.grid(column=2,row=1,padx=20,pady=20)



statusbar = Label(window, text="Thank you for using our system. - Comp2073", relief=SUNKEN, anchor=W)
statusbar.config(font=("Courier", 10,"bold"))
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()