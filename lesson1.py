import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#create window
window = tk.Tk()
window.geometry("500x450")
window.title("Welcome to New Application")


def buttonFunction():
    print("push button")

    #label
    label.config(text="Have Fun!",font="Times 25",bg="red",fg="black")
   
    #entry
    value = entry.get()
    print(value)
    label.config(text=value)
    entry.config(state="disabled")
    #message
    #message_box = messagebox.showinfo(title="info",message="information")
    #message_box = messagebox.askretrycancel(title="info",message="information")
    #message_box = messagebox.askquestion(title="info",message="information")
    #message_box = messagebox.askyesnocancel(title="info",message="information")
    message_box = messagebox.showerror(title="info",message="information")   
    print(message_box)

#button
button = tk.Button(window, text = "First Button", activebackground = "blue",
                   bg="red",fg="white",activeforeground="black",
                   height=15,width=50,command=buttonFunction)
button.pack() #geometry manager 


#label
label = tk.Label(window,text="Hi World",font="Times 16",fg="white",
                 bg="black",wraplength=150)
label.pack(side = tk.RIGHT,padx=25)


#entry
entry = tk.Entry(window,width=50)
entry.insert(index=0, string= "Write your name only one more time.")
entry.pack(side=tk.LEFT,padx=25)


window.mainloop()

