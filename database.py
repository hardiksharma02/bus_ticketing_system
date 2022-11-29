import sqlite3

con=sqlite3.connect('Bus_Book.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS OPERATOR(OPid int(2),Name varchar(20),Address varchar(50),Email varchar(20),PhoneNo int(20),Primary Key(OPid))')
cur.execute('CREATE TABLE IF NOT EXISTS ROUTE(RouteID int(2),SId int(2),SName varchar(20),Primary Key(RouteID,SId))')
cur.execute('CREATE TABLE IF NOT EXISTS BUS(BId int(2),BType varchar(20),Capacity int(3),Fare int(4),OPid int(2),RouteID int(2),Primary Key(BId))')
cur.execute('CREATE TABLE IF NOT EXISTS RUNS(BusId int(2),Runs_Date varchar(12),Seat_Avail int(2),Primary Key(BusId,Runs_Date))')
cur.execute('CREATE TABLE IF NOT EXISTS BookHistory(BookId int(2),Passenger_Name varchar(20),Gender varchar(6),No_of_Seats int(1),PhoneNo int(20),Age int(2),BusID int(2),Fare int,TravelDate Date,BoardingPoint varchar(20),DestinationPoint varchar(20),Primary Key(BookId))')
cur.execute('insert into OPERATOR(OPid,Name,Address,Email,PhoneNo) values(1,"Kamla Travels","Prayagraj,UP","kamlatravels@gmail.com",8423476001),(2,"Hans Travels","Lucknow,UP","hanstravels@gmail.com",9305846926),(3,"Volvo","Varanasi,UP","Volvo@gmail.com",7538291753)')
cur.execute('insert into ROUTE(RouteID,SId,SName) values(1,1,"Guna"),(1,2,"JP College"),(1,3,"Binaganj"),(1,4,"Biora"),(1,5,"Bhopal"),(2,1,"Bhopal"),(2,2,"Biora"),(2,3,"Binaganj"),(2,4,"JP College"),(2,5,"Guna"),(3,1,"Delhi"),(3,2,"Agra"),(3,3,"Jhansi"),(3,4,"Shivpuri"),(3,5,"Guna"),(3,6,"JP College"),(4,1,"JP College"),(4,2,"Guna"),(4,3,"Shivpuri"),(4,4,"Jhansi"),(4,5,"Agra"),(4,6,"Delhi")')
cur.execute('insert into BUS(BId,BType,Capacity,Fare,OPid,RouteID) values(1,"AC",30,900,1,1),(2,"Non AC",50,400,1,2),(3,"AC",50,1500,3,3),(4,"Non AC",60,800,2,3),(5,"AC",30,1700,2,4)')
cur.execute('insert into RUNS(BusId,Runs_Date,Seat_Avail) values(1,"01-12-2022",30),(1,"02-12-2022",30),(1,"03-12-2022",30),(1,"04-12-2022",30),(1,"05-12-2022",30),(2,"01-12-2022",50),(2,"02-12-2022",50),(2,"03-12-2022",50),(2,"04-12-2022",50),(2,"05-12-2022",50),(3,"01-12-2022",50),(3,"02-12-2022",50),(3,"03-12-2022",50),(3,"04-12-2022",50),(3,"05-12-2022",50),(4,"01-12-2022",60),(4,"02-12-2022",60),(4,"03-12-2022",60),(4,"04-12-2022",60),(4,"05-12-2022",60),(5,"01-12-2022",30),(5,"02-12-2022",30),(5,"03-12-2022",30),(5,"04-12-2022",30),(5,"05-12-2022",30)')

cur.close()