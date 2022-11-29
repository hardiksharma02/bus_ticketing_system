from tkinter import *
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,k))
def close():
    root.destroy()
    import home
root.title("Bus Ticketing System")
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w//3+10)
Label(root,text="Online Bus Ticketing System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=0,padx=w//3+10)
Label(root,text="Name: Hardik Sharma",fg='blue',font='Arial 12 bold').grid(row=10,column=0,padx=w//3+10,pady=(50,10))
Label(root,text="Er:211B126",fg='blue',font='Arial 12 bold').grid(row=14,column=0,padx=w//3+10,pady=(50,10))
Label(root,text="Mobile:9799444332" ,fg='blue',font='Arial 12 bold').grid(row=15,column=0,padx=w//3+10,pady=(50,10))
Label(root,text="Submitted To: Dr. Mahesh Kumar",fg='red',bg='LightSkyBlue1',font='Arial 12 bold').grid(row=20,column=0,padx=w//3+10,pady=(50,10))
Label(root,text="Project Based Learning",fg='red',font='Arial 12 bold').grid(row=25,column=0,padx=w//3+10,pady=(50,10))
root.after(5000,close)
root.mainloop()
