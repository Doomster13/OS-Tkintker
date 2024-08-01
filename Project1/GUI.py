import tkinter as tk
import os
win = tk.Tk()
win.title("File Creater/Remover")
win.geometry("270x300")
def click1():
    win2 = tk.Tk()
    win2.title("Creater")
    def B2():
        a=Entry1.get()
        b=Entry2.get()
        os.mkdir (f"{b}/{a}")
        l=tk.Label(win2,text=f"File {Entry1.get()} created")
        l.pack()

    win2.geometry("300x150")
    label1=tk.Label(win2,text="Enter name of the file you want to make")
    label1.pack()
    
    Entry1=tk.Entry(win2)
    Entry1.pack()
    
    label2=tk.Label(win2,text="where do you want the file to be?")
    label2.pack()
    
    Entry2=tk.Entry(win2)
    Entry2.pack()
    
    b2 = tk.Button(win2,text="Proceed",command=B2)
    b2.pack()
    
def click2():
    win2 = tk.Tk()
    win2.title("Remover")
    win2.geometry("300x150")
    def B():
        a=Entry1.get()
        b=Entry2.get()
        os.rmdir (f"{b}/{a}")
        l=tk.Label(win2,text=f"File {Entry1.get()} deleted")
        l.pack()
        
    label1=tk.Label(win2,text="Enter name of the file you want to delete?")
    label1.pack()
    
    Entry1=tk.Entry(win2)
    Entry1.pack()
    
    label2=tk.Label(win2,text="where is the file?")
    label2.pack()
    
    Entry2=tk.Entry(win2)
    Entry2.pack()
    
    b=tk.Button(win2,text="Proceed",command=B)
    b.pack()
    
    win2.mainloop()
    
button1 = tk.Button(win,text="Create File",command = click1)
button1.grid(row=0, column=0, sticky='nsew', pady=50,padx=100)
button2 = tk.Button(win,text="Delete File",command = click2)
button2.grid(row=1, column=0, sticky='nsew',pady=50,padx=100)

win.mainloop()