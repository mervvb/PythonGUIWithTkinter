import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.geometry("800x600")
#menu
def fileFunction(selectedItem):   
    print(selectedItem)
def editFunction(selectedItem):
    print(selectedItem)


menubar = tk.Menu(window)
window.config(menu = menubar)

file = tk.Menu(menubar)
edit = tk.Menu(menubar)

menubar.add_cascade(menu=file,label="file")
"""add_cascade (seçenek) : Üst menü öğesi ekler. add_command (seçenekler)
 : Menü öğesi ekler. add_separator(): Menüler arasına çizgi ekler."""

menubar.add_cascade(menu=edit,label="edit")

file.add_command(label="new file",command=lambda:fileFunction("new file"))
edit.add_command(label="undo",command=lambda:editFunction("undo"))
file.add_command(label="open",command=lambda:fileFunction("open"))
edit.add_command(label="paste",command=lambda:editFunction("paste"))
file.add_command(label="print",command=lambda:fileFunction("print"))
edit.add_command(label="select all",command=lambda:editFunction("select all"))

menubar.add_separator()
file.add_separator()
edit.add_separator()

#tabs

tabs = ttk.Notebook(window,width=540,height=300)

tabs.place(x=25,y=25)

tab1 = ttk.Frame(tabs,width=50,height=50)
tab2 = ttk.Frame(tabs,width=50,height=50)
tab3 = ttk.Frame(tabs,width=50,height=50)

tk.Label(tab1,text="tab1").grid(row=0,column=0,padx=270,pady=0)
tk.Label(tab2,text="tab2").pack()
tk.Label(tab3,text="tab3").grid(row=0,column=0)


tabs.add(tab1,text="treeview")
tabs.add(tab2,text="list box")
tabs.add(tab3,text="text editor")

#treeview


treeview = ttk.Treeview(tab1)
treeview.place(x=5,y=5)


treeview.insert("", "0", "item1",text="Spain")
treeview.insert("item1", "1", "item2",text="Madrid")
treeview.insert("", "2", "item3",text="France")
treeview.insert("item3", "3", "item4",text="Paris")


# Çift tıklama olayını işleyen bir işlev tanımla
def callBack(event): 
    item=None
    item = treeview.identify("item",event.x,event.y)
    print(item)

# Çift tıklama olayını Treeview widget'ına bağla
treeview.bind("<Double-1>", callBack)



#listbox

def getItem():
    index_list = listbox.curselection()
    print(index_list)
    for i in index_list:
        print(listbox.get(i))


listbox = tk.Listbox(tab2,selectmode=tk.MULTIPLE)
listbox.insert(0,"Spain")
listbox.insert(1,"England")
listbox.insert(2,"France")
listbox.place(x=5,y=5)

button = tk.Button(tab2,text="button",command=getItem)
button.place(x=150,y=5)


#text editor
def textFunction():    
    print(texteditor.get(1.0,tk.END))

texteditor = tk.Text(tab3,width=20,height=20,wrap=tk.WORD)
texteditor.grid(row=0,column=0,padx=10,pady=10)
button = tk.Button(tab3,text="save",command=textFunction)
button.grid(row=0,column=2,padx=10,pady=10)



#scrollbar

scroll = tk.Scrollbar(tab3,orient=tk.VERTICAL,command=texteditor.yview)
scroll.grid(row=0,column=1,sticky=tk.N + tk.S)

texteditor.config(yscrollcommand=scroll.set)


window.mainloop()
