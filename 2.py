from Tkinter import *
# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *
import math
import string

def Plus():
    x1= float(Entry.get(x))
    y1= float(Entry.get(y))
    xy= x1+y1
    print xy

root = Tk()
x= Entry(root)
x.grid(row=0, column=0)

y= Entry(root)
y.grid(row=1, column=0)

Button(root, text="Dodaj", command=Plus).grid(row=2, column=0)

mainloop()
