import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#create window
window = tk.Tk()
window.geometry("600x500")
window.title("Welcome to New Application")

def buttonFunction():
    print("here")
    m = Method.get()
    if m == "1" :
        print("method1")
    elif m == "2":
        print("method2")
    else:
        print("method1&method2")
    p = Problem.get()
    print(p)
    value1 = save_var1.get()
    value2 = save_var2.get()
    if value1 == 1:
        print("save")
    elif value2 == 1:
        print("not save")
   


button = tk.Button(window,text="button1",activebackground="black",bg="grey"
                   ,activeforeground="green",fg="cyan",height=15,
                   width=50,command=buttonFunction)

button.grid(row=0,column=0,pady=15)


#radiobutton

Method = tk.StringVar()

tk.Radiobutton(window,variable=Method,value="1",text="method1",activebackground="pink"
               ,bg="black",activeforeground="red",fg="purple",height=5
               ,width=5,borderwidth=15).grid(row=1,column=0,pady=15)
tk.Radiobutton(window,variable=Method,value="2",text="method2",activebackground="cyan"
               ,bg="purple",activeforeground="red",fg="pink",height=5
               ,width=5,borderwidth=15).grid(row=1,column=1,pady=15)


#combobox

Problem = tk.StringVar()

combobox = ttk.Combobox(window,textvariable=Problem,values=("1","2","3"),
                        state="readonly")

combobox.grid(row=2,column=0,pady=15)


#checkbutton

def checkButtonFunction():
    print("clicked by admin")

save_var1 = tk.IntVar()
save_var2 = tk.IntVar()

c_button1 = tk.Checkbutton(window,text="save",offvalue=0,
                          variable=save_var1, font="Times 25",
                          activebackground="yellow",bg="pink",
                          activeforeground="white",fg="black",
                          command=checkButtonFunction)
c_button1.grid(row=2,column=1,pady=15)

c_button2 = tk.Checkbutton(window,text="not save",offvalue=0,
                          variable=save_var2, font="Times 25",
                          activebackground="yellow",bg="pink",
                          activeforeground="white",fg="black",
                          command=checkButtonFunction)


c_button2.grid(row=2,column=2,pady=15)


window.mainloop()

