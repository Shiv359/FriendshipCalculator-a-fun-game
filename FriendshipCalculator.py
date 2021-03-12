from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("655x433")
root.title("Dosti ka Calculator")

def calculate():
    print(f"{yname.get()},{fname.get()}")
    name=yname.get().lower()
    f_name=fname.get().lower()
    print(name,f_name)
    n = name + f_name
    c = 0
    for i in n:
        if i in "aeiou":
            c += 5
        elif i in "friends":
            c += 2
        else:
            c += 2
    if c > 75:
        print(c)
        print("Made for each other")
        tmsg.showinfo("Dosti", "Made for each other")
    elif c >=50 and c < 75:
        print(c)
        print("Best Friends")
        tmsg.showinfo("Dosti", "Best Friends")
    else:
        print(c)
        print("Friends")
        tmsg.showinfo("Dosti","Friends")

l1=Label(root,text="Dosti ka Meter",font="Ariel 20 bold",fg="grey",bg="pink")
l1.grid()
l2=Label(root,text="Your Name",font="9")
l2.grid(row=1,column=0)

l3=Label(root,text="Your Friends Name",font="9")
l3.grid(row=2,column=0)

yname=StringVar()
fname=StringVar()

yentry=Entry(root,textvariable=yname)
yentry.grid(row=1,column=1)
fentry=Entry(root,textvariable=fname)
fentry.grid(row=2,column=1)

b1=Button(root,text="Calculate",command=calculate)
b1.grid(row=3,column=1)






root.mainloop()