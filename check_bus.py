from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,k=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,k))
root.title("Bus Ticketing System")
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=5,padx=w//10)
Button(root,text="Online Bus Booking System",font='Arial 14 bold',fg='red',bg='LightSkyBlue1').grid(row=1,column=1,columnspan=5,padx=w//3-50)
Button(root,text="Check Your Booking",font='Arial 14 bold',fg='black',bg='Green2').grid(row=5,column=1,columnspan=20,padx=w//3)
Label(root,text='Enter your Mobile No.',font='Arial 12 bold').grid(row=7,column=2,rowspan=5,pady=50,sticky=E)
mobile=Entry(root)
mobile.grid(row=7,column=3,pady=50,columnspan=1,padx=w//10-120,sticky=W)
def fun():
    if len(mobile.get())==0:
        showerror('Value Missing',"Please Enter a valid Mobile Number")
Button(root,text="Check Booking",font='Arial 12 bold',command=fun).grid(row=7,column=4,pady=50,rowspan=10)
root.mainloop()
