import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#create window
window = tk.Tk()
#%%
#main frames

frame_left = tk.Frame(window,width=540,height=640,bg="black")
frame_left.grid(row=0,column=0,padx=10,pady=10)

frame_right = tk.Frame(window,width=540,height=640,bg="green")
frame_right.grid(row=0,column=1,padx=10,pady=10)


frame1 = tk.LabelFrame(frame_left,text="Frame1",width=540,height=500,bg="red")
frame1.grid(row=0,column=0,padx=10,pady=10)

frame2 = tk.LabelFrame(frame_left,text="Frame2",width=540,height=140,bg="blue")
frame2.grid(row=1,column=0,padx=10,pady=10)

label1 = tk.Label(frame2,text="label in frame2")
label1.grid(row=0,column=0,padx=10,pady=10)

window.mainloop()

#%%
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#create window
window = tk.Tk()

pw = ttk.Panedwindow(window,orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH,expand=True)

m2 = ttk.Panedwindow(pw,orient=tk.VERTICAL)


frame2 = ttk.Frame(pw,width=720,height=400,relief=tk.RIDGE)
frame3 = ttk.Frame(pw,width=720,height=240,relief=tk.RAISED)

frame1 = ttk.Frame(pw,width=360,height=640,relief=tk.GROOVE)

m2.add(frame2)
m2.add(frame3)
pw.add(frame1)
pw.add(m2)

window.mainloop()
