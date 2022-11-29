from tkinter import *
from tkinter.messagebox import *

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0" %(w,h))
root.title("Online Bus Booking System: Add Details")

bus=PhotoImage(file="Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=15,padx=(w-256)/2)

Title=Label(root,font=('aria',30,'bold'),text="Online Bus Booking System",fg="Red",bd=10,bg="light sky blue")
Title.grid(row=1,column=0,columnspan=15)

details=Label(root,font=('aria',15,'bold'),text="Bus Ticket")
details.grid(row=2,column=0,columnspan=15,pady=(50,50))

frame=Frame(root,highlightbackground='Black',highlightthickness=2,height=100,width=500)
frame.grid(row=5,column=5,columnspan=5)
Label(frame,text='Passenger:',font=('aria',15,'bold')).grid(row=0,column=1)
Label(frame,text='',font=('aria',15,'bold')).grid(row=0,column=2)
Label(frame,text='Gender:',font=('aria',15,'bold')).grid(row=0,column=3)
Label(frame,text='',font=('aria',15,'bold')).grid(row=0,column=4)

booked=showinfo('Success','Seat Booked...')
if(booked=='ok'):
    showinfo('Thanks','Thank you for using Python bus service')

root.mainloop()