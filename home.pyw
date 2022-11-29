from tkinter import *
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
def home():
    root.destroy
    import home 
def seat():
    root.destroy()
    import seat_booking
def booked():
    root.destroy()
    import check_bus
def add():
    root.destroy()
    import add_bus_detail
root.geometry('%dx%d+0+0'%(w,k))
root.title("Bus Ticketing System")
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=5,padx=w//3)
Button(root,text="Online Bus Ticketing System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=0,columnspan=5,padx=w//3)
Button(root,text="Seat Booking",font='Arial 14 bold',fg='black',bg='Green2',command=seat).grid(row=4,column=0,padx=100,pady=40)
Button(root,text="Checked Book Seat",font='Arial 14 bold',fg='black',bg='Green3',command=booked).grid(row=4,column=1)
Button(root,text="Add Bus details",font='Arial 14 bold',fg='black',bg='Green4',command=add).grid(row=4,column=2)
Label(root,text="For admin only",fg='red').grid(row=5,column=2)
root.mainloop()
