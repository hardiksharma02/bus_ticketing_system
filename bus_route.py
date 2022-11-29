from tkinter import *
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,k))
root.title("Bus Ticketing System")
def home():
    root.destroy()
    import home
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=w//3)
Button(root,text="Online Bus Ticketing System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Add Bus Route Details',font='Arial 20 bold',fg='green').grid(row=3,column=0,columnspan=10,padx=w//3,pady=50)
Label(root,text='Route Id',font='Arial 12 bold').grid(row=7,column=0,sticky=E)
Entry(root).grid(row=7,column=1,sticky=W)
Label(root,text='Station Name',font='Arial 12 bold').grid(row=7,column=2,sticky=E)
Entry(root).grid(row=7,column=3,sticky=W)
Label(root,text='Station Id ',font='Arial 12 bold').grid(row=7,column=4,sticky=E)
Entry(root).grid(row=7,column=5,sticky=W)
Button(root,text="Add Route",font='Arial 14 bold',fg='black',bg='Green2').grid(row=7,column=6)
Button(root,text="Delete Route",font='Arial 14 bold',fg='black',bg='Orange').grid(row=7,column=7)
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1,command=home).grid(row=8,column=7)
root.mainloop()
