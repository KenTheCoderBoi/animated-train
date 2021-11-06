from tkinter import *
import random

root=Tk()
root.title("jendikjnc")
root.geometry("400x400")

enter = Entry(root)
enter.place(relx=0.5,rely=0.2,anchor=CENTER)

label1 = Label(root)
label1.place(relx=0.5,rely=0.4,anchor=CENTER)

label2 = Label(root)
label2.place(relx=0.5,rely=0.6,anchor=CENTER)

label3 = Label(root)
label3.place(relx=0.5,rely=0.65,anchor=CENTER)


list1 = []
def addfriendcommand():
    name = enter.get()
    list1.append(name)
    label1["text"] = list1
def randomfriend():
    length = len(list1)
    randomnum= random.randint(0,length-1)
    label2["text"] = list1[randomnum]
    label3["text"] = randomnum
    
addfriend = Button(root,text="add friend", command=addfriendcommand,anchor=CENTER)
addfriend.place(relx=0.4,rely=0.3)
randomint = Button(root,text="random friend", command=randomfriend,anchor=CENTER)
randomint.place(relx=0.4,rely=0.7)

root.mainloop()