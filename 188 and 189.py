from tkinter import *

root = Tk()
root.title("TitleyThingy?")
root.geometry("400x250")


label = Label(root,text = "What Should I Type?")
label.pack()

entry = Entry(root)
entry.pack()


label1 = Label(root,text = "What Should I Typfghe?")
label1.pack()

entry1 = Entry(root)
entry1.pack()


def hyu():
    try:
     text1 = int(entry.get())
     text2 = int(entry1.get())
     messagebox.showinfo("error","no error accepted")
    except:
        messagebox.showinfo("accepted","Telling accepted is unacceptable and acceptable which is unaccaptable which is acceptable which in acceptable and lastly it is not aceptable")
        

btn = Button(root,text = "Click me", command = hyu)
btn.pack()
root.mainloop()






















