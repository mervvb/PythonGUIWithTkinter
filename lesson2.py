import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Geometry Manager")


#pack
red = tk.Button(window,text="Pack1",fg="red")
red.pack(side=tk.LEFT)

green = tk.Button(window,text="Pack2",fg="green")
green.pack(side=tk.LEFT)

blue = tk.Button(window,text="Pack3",fg="blue")
blue.pack(side=tk.BOTTOM)

purple = tk.Button(window,text="Pack4",fg="purple")
purple.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

#%%
#grid
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
"""
window.title("Geometry Manager")

for r in range(5):
    for c in range(5):
        label = tk.Label(window,text='R%s/C%s'%(r,c),borderwidth=2)
        label.grid(row=r,column=c,padx=3,pady=3)
"""

 
# creating main tkinter window/toplevel
window = tk.Tk()
 
# this will create a label widget
l1 = tk.Label(window, text = "First:")
l2 = tk.Label(window, text = "Second:")
 
# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, pady = 2)
l2.grid(row = 1, column = 0, pady = 2)
 
# entry widgets, used to take entry from user
e1 = tk.Entry(window)
e2 = tk.Entry(window)
 
# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
 
# infinite loop which can be terminated by keyboard
# or mouse interrupt
window.mainloop()
#%%

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Geometry Manager")

label1 = tk.Label(window,text="place1")
label1.place(x=150,y=150)

label2 = tk.Label(window,text="place2")
label2.place(x=300,y=300)

label3 = tk.Label(window,text="place3")
label3.place(relx=0.5,rely=0.5)

window.mainloop()

#%%
