from tkinter import *
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,k))
options = [
    "Male",
    "Female",
    "Others",
]
def book():
    Button(root,text="Fill Passanger Details to Book Bus Ticket",bg='SkyBlue',fg='Red',font='arial 14 bold').grid(row=9,column=2,columnspan=20)
    Label(root,text="Name",font='Arial 14 bold').grid(row=10,column=1,sticky=E)
    Entry(root).grid(row=10,column=2,sticky=W)
    Label(root,text="Gender",font='Arial 14 bold').grid(row=10,column=3,sticky=E)
    clicked = StringVar()
    clicked.set( "Male" )
    drop = OptionMenu( root ,clicked,*options )
    drop.grid(row=10,column=4,sticky=W)
    Label(root,text="No. of tables",font='Arial 14 bold').grid(row=10,column=5,sticky=E)
    Entry(root).grid(row=10,column=6,sticky=W)
    Label(root,text="Mobile No.",font='Arial 14 bold').grid(row=10,column=7,sticky=E)
    Entry(root).grid(row=10,column=8,sticky=W)
    Label(root,text="Age",font='Arial 14 bold').grid(row=10,column=9,sticky=E)
    Entry(root).grid(row=10,column=10,sticky=W)
    Button(root,text="Book Seat",fg='Green',bg="White").grid(row=10,column=11,sticky=E)
def Show():
    Label(root,text="Select Bus",font='Arial 14 bold',fg='Green').grid(row=5,column=1,sticky=E)
    Label(root,text="Operator",font='Arial 14 bold',fg='Green').grid(row=5,column=2,sticky=E)
    Label(root,text="Bus Type",font='Arial 14 bold',fg='Green').grid(row=5,column=3,sticky=E)
    Label(root,text="Available/Capacity",font='Arial 14 bold',fg='Green').grid(row=5,column=4,sticky=E)
    Label(root,text="Fare",font='Arial 14 bold',fg='Green').grid(row=5,column=5,sticky=E)
    Button(root,text="Proceed To Book",font='Arial 14 bold',fg='Black',bg='Green',command=book).grid(row=6,column=6,sticky=E)
root.title("Bus Ticketing System")
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=15,padx=w//2.5)
Button(root,text="Online Bus Ticketing System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=1,columnspan=20)
Button(root,text="Enter Journey Details",font='Arial 14 bold',fg='red',bg='lightgreen').grid(row=2,column=1,columnspan=20)
Label(root,text="To",font='Arial 14 bold',fg="black").grid(row=3,column=1,sticky=E)
Entry(root).grid(row=3,column=2,sticky=W)
Label(root,text="From",font='Arial 14 bold').grid(row=3,column=3,sticky=E)
Entry(root).grid(row=3,column=4,sticky=W)
Label(root,text="Journey Date",font='Arial 14 bold').grid(row=3,column=5,sticky=E)
Entry(root).grid(row=3,column=6,sticky=W)
Button(root,text='SHOW BUSES',fg='Black',bg='Green',command=Show).grid(row=3,column=7)
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1).grid(row=3,column=8)

root.mainloop()
