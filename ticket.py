from tkinter import *
from tkinter.messagebox import *
import sqlite3
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,k))
root.title("Bus Ticketing System")
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=15,padx=w//2.5)
Button(root,text="Online Bus Ticketing System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=1,columnspan=20)
root.mainloop()