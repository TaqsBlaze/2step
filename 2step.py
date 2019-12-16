#A 2 step login
#IOTECH SOFTWARE
import os
import sys
import time
import sqlite3 as sql
from Tkinter import *



class About:
	def __init__(self,version='1.0',name='2steplogin'):
		self.version = version
		self.name = name

class Window:
#Here the user logs in 
	def __init__(self):
	
		self.window = Tk()

	def init(self):
		self.window.attributes("-toolwindow",True)
		self.window.config(bg="white")
		self.window.geometry("580x450+350+150")
		self.window.maxsize(580,450)
		self.window.minsize(580,450)
		self.window.title("2 step login")
		password = StringVar()
		label = Label(self.window,text="Log in",font="Shrutil 13",bg="white")
		label.pack(fill=BOTH)

		indicator = Label(self.window,text='')
		indicator.config(bg="White")
		indicator.place(x=250,y=110)
		PassWord = Entry(self.window,textvariable=password)
		PassWord.config(border=2,relief=GROOVE,font="Shrutil 14 bold",show="*",width=25)
		PassWord.place(x=150,y=160)
		PassWord.focus()

		LogIn = Button(self.window,text="Login",font="Shrutil 10",command=_LogIn(PassWord,self.window).login)
		LogIn.config(bg="#44E3A3",fg="white",width=14,border=1,relief=GROOVE)
		LogIn.place(x=230,y=200)


		self.window.mainloop()
		

class _LogIn:
#In here we login
#check if the entered password matches the password in the database
	def __init__(self,password,window):
		self.password = password
		self.window = window
	def login(self):
		
		db = sql.connect("users.sql")
		
		get_pass = db.execute("SELECT PASSWORD FROM ME")
		for i in get_pass:
			password = i[0]
		db.close()
		if(self.password.get() == password):
			self.password.config(bg="#90EE90")
			self.window.destroy()
		else:
			self.password.config(bg="#FF9797")
			pass


class SetUp:
#Here the user sets the password
	def __init__(self):
		self.setwin=Tk()
		
	def SetPassword(self):
		self.setwin.geometry("580x450+350+150")
		self.setwin.maxsize(580,450)
		self.setwin.minsize(580,450)
		self.setwin.title("")
		self.setwin.attributes("-toolwindow",True)
		Step_2 = StringVar()
		self.setwin.config(bg="white")
		
		
		Label(self.setwin,text="Set your 2 step login password",bg="white",font="shrutil 11",fg="black").pack(fill=BOTH)
		
		step_2 = Entry(self.setwin,textvariable=Step_2,width=30)
		step_2.config(border=2,relief=GROOVE,font="Shrutil 12",show=None)
		step_2.place(x=150,y=160)
		setb = Button(self.setwin,text="Set>",command=SetPass(step_2).Set)
		setb.config(bg="#44E3A3",fg="white",width=14,border=1,relief=GROOVE)
		setb.place(x=240,y=200)
		step_2.focus()
		self.setwin.mainloop()
		
		
class SetPass:
#In here we set the password in the database
	def __init__(self,password):
		self.password = password
	def Set(self):
		
		db = sql.connect("users.sql")
		db.execute('''CREATE TABLE ME
				(ID INT PRIMARY KEY NOT NULL,
				PASSWORD TEXT NOT NULL);''')

		db.execute('''INSERT INTO ME (ID,PASSWORD) \
				VALUES (1, '{}');'''.format(self.password.get()))
		db.commit()
		db.close()
		f=open("set.sql","w")
		f.write("#Set")
		f.close()
		
		
		
check = open("set.sql","r+")
check = check.read()
time.sleep(2)

if(len(check) < 1):
	SetUp().SetPassword()
else:
	pass
Window().init()
