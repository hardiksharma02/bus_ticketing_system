from tkinter import *
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,k))
root.title("Bus Ticketing System")
def new_op():
    root.destroy()
    import bus_operator
def new_bus():
    root.destroy()
    import bus_detail
def new_route():
    root.destroy()
    import bus_route
def newrun():
    root.destroy()
    import new_run
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=5,padx=w//3)
Button(root,text="Online Bus Ticketing System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=0,columnspan=5,padx=w//3)
Label(root,text='Add New Details to database',font='Arial 14 bold',fg='green',).grid(row=2,column=0,columnspan=5,padx=w//3)
Button(root,text="New Operator",font='Arial 14 bold',fg='black',bg='Green2',command=new_op).grid(row=5,column=0,padx=100,pady=40)
Button(root,text="New Bus",font='Arial 14 bold',fg='black',bg='Orange',command=new_bus).grid(row=5,column=1)
Button(root,text="New Route",font='Arial 14 bold',fg='black',bg='Lightblue',command=new_route).grid(row=5,column=2)
Button(root,text="New Run",font='Arial 14 bold',fg='black',bg='Pink',command=newrun).grid(row=5,column=3)
root.mainloop()
