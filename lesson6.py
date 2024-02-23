import tkinter as tk 
from tkinter import filedialog
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("800x800")

#file dialog(open file)

def openFile():
    file_name = filedialog.askopenfilename(initialdir= "D:\\anacondaDers1",
                                           title="select a file")
    """
    Başlangıç dizini: Başlangıç dizinini belirtirken çift ters eğik çizgiyi ("\") 
    kullanmanız gerekmektedir. Bu, kaçış karakteri olarak kullanıldığından,
    tek bir ters eğik çizgi kullanırsanız hata alabilirsiniz.
    """
    print(file_name)
    Img = Image.open(file_name)
    Img = ImageTk.PhotoImage(Img)#*
    """
    Resim nesnesi sızdırması: Kodunuzda, ImageTk.PhotoImage nesnesini Img
    adlı bir değişkene atadıktan sonra, bu nesnenin tutulması gerekiyor.
    Aksi takdirde, Python'un çöp toplama işlemi bu nesneyi bellekten temizleyebilir.
    Bu nedenle, Img nesnesini bir değişkende saklamanız gerekiyor.
    """
    
    label = tk.Label(window,image=Img)
    label.image = Img
    label.pack(padx=15,pady=15)

button = tk.Button(window,text="open file",command=openFile)
button.pack()

window.mainloop()

#%%
#plot
import tkinter as tk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

window = tk.Tk()
window.geometry("500x800")


fig = Figure(figsize=(5,4),dpi=50)
data = np.arange(0,3,0.1)

fig.add_subplot(111).plot(data,data*2+10)

canvas = FigureCanvasTkAgg(fig,master=window)

canvas.draw()
canvas.get_tk_widget().pack()

def leftClick(event):
    tk.Label(window,text="left").pack()

def middleClick(event):
    tk.Label(window,text="middle").pack()

def rightClick(event):
    tk.Label(window,text="right").pack()
    

window.bind("<Button-1>",leftClick)
window.bind("<Button-2>",middleClick)
window.bind("<Button-3>",rightClick)



window.mainloop()

# %%
