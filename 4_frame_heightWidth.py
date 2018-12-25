from tkinter import *

root = Tk()
frame1 = Frame(root, width = 300, height = 200)
lable1 = Label(frame1, text = "This is frame 1")

lable1.pack()
frame1.pack()
root.mainloop()