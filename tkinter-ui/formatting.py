from tkinter import *
root = Tk()


frame = Frame(root)

Label(frame, text="Pack Demo of side and fill").pack()
Button(frame, text="A").pack(side=LEFT, fill=Y)
Button(frame, text="B").pack(side=TOP, fill=X)
Button(frame, text="C").pack(side=RIGHT, fill=NONE)
Button(frame, text="D").pack(side=TOP, fill=NONE)

frame.pack()


Label(root, text="Pack Demo of Expand").pack()
Button(root, text="I do not expand.").pack()
Button(root, text="I do not fill x but I expand").pack(expand=1)
Button(root, text="I fill x and expand").pack(fill=X, expand=1)
root.mainloop()
