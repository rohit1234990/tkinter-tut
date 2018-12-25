from tkinter import *

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

label1 = Label(frame1, text = "This is frame 1")
label2 = Label(frame2, text = "This is frame 2")

label1.pack()
label2.pack()

frame1.pack()
frame2.pack(side = BOTTOM)

root.mainloop()