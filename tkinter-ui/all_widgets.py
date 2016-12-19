from tkinter import *

'''
Label(parent, text="Enter your password.")
Button(parent, text="Search")
Checkbutton(parent, text="Remember Me", variable=v, value=True)
Entry(parent, width=30)
Radiobutton(parent, text="Male", variable=v, value=1)
Radiobutton(parent, text="Female", variable=v, value=2)
OptionMenu(parent, var, "Select Country", "USA", "UK", "India", "Others")
Scrollbar(parent, orient=VERTICAL, command=text.yview)
'''

root = Tk()
Toplevel(root).pack_slaves() # ?
Canvas(root).pack()
v = None
om = OptionMenu(root, variable=v, value="Memory").pack()
# Menu(om).pack()
# Frame
# Scale
# Text
# Checkbutton
# LabelFrame
# Menubutton
# PanedWindow
# Scrollbar
# Bitmap
# Button
# Entry
# Listbox
# Message
# Radiobutton
# Spinbox
# Image class
Label(root, text="I come pre-packed").pack()
root.mainloop()

# WIDGET - name(its_parent, **its_configuration_options)