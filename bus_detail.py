from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,k))
root.title("Bus Ticketing System")
def done():
    showinfo('bus entry',"Bus Record added")
def home():
    root.destroy()
    import home
options = [
    "AC 2X2",
    "AC 3X2",
    "Non AC 2X2",
    "Non AC 3X2",
    "AC Sleeper 2X1",
    "Non-AC Sleeper 2X1",
]
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=w//3)
Button(root,text="Online Bus Ticketing System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Add Bus Details',font='Arial 20 bold',fg='green').grid(row=3,column=0,columnspan=10,padx=w//3,pady=50)
Label(root,text='Bus Id',font='Arial 12 bold').grid(row=7,column=0,sticky=E)
Entry(root).grid(row=7,column=1,sticky=W)
Label(root,text='Bus Type',font='Arial 12 bold').grid(row=7,column=2,sticky=E)
clicked = StringVar()
clicked.set( "AC 2X2" )
drop = OptionMenu( root ,clicked,*options )
drop.grid(row=7,column=4,sticky=W)
Label(root,text='Capacity',font='Arial 12 bold').grid(row=7,column=4,sticky=E)
Entry(root).grid(row=7,column=5,sticky=W)
Label(root,text='Fare Price Rs.',font='Arial 12 bold').grid(row=7,column=6,sticky=E)
Entry(root).grid(row=7,column=7,sticky=W)
Label(root,text='Operator Id',font='Arial 12 bold').grid(row=7,column=8,sticky=E)
Entry(root).grid(row=7,column=9,sticky=W)
Label(root,text='Route Id',font='Arial 12 bold').grid(row=7,column=9,sticky=E)
Entry(root).grid(row=7,column=10,sticky=W)
Button(root,text="ADD",font='Arial 14 bold',fg='black',bg='Green2',command=done).grid(row=8,column=5)
Button(root,text="EDIT",font='Arial 14 bold',fg='black',bg='Orange').grid(row=8,column=6)
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1,command=home).grid(row=8,column=7)
root.mainloop()
