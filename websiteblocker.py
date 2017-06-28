import flask
from tkinter import *
import time
from datetime import datetime as dt
import admin
import sys
#if not admin.isUserAdmin():
	#print("Ye BOi")
	#admin.runAsAdmin()
class websiteBlocker(object):
	def __init__(self):
		self.website_list=[]
		self.time1=8
		self.time2=16

	def setWebsites(self,website):
		self.website_list+=[str(website)]
	def setTime(self,time1,time2):
		self.time1=int(time1)
		self.time2=int(time2)	

	def getWebsites(self):
		return self.website_list

	def getTime(self):
		return self.time1,self.time2


	def block(self):
		hosts_path="C:\WINDOWS\System32\drivers\etc\hosts"
		redirect="127.0.0.1"
		#self.website_list=["www.facebook.com","facebook.com"]

		while True:
			if dt(dt.now().year,dt.now().month,dt.now().day,self.time1)< dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,self.time2):
				print("Working hours blocking %s"%(self.website_list))
				with open(hosts_path,"r+") as file:
					content=file.read()
					for website in self.website_list:
						if website in content:
							pass
						else:
							file.write(redirect+" "+website+"\n")
			else:
				with open(hosts_path,"r+") as file:
					content=file.readlines()
					file.seek(0)
					for line in content:
						if not any(website in line for website in self.website_list):
							file.write(line)
					file.truncate()

				print("Fun hours....")


			time.sleep(5)

	def reverse(self):
		with open(hosts_path,"r+") as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in self.website_list):
					file.write(line)
			file.truncate()
		print("Fun hours ....")




"""
hosts_path="C:\WINDOWS\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,18):
		print("Working hours")
		with open(hosts_path,"r+") as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")
	else:
		with open(hosts_path,"r+") as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()

		print("Fun hours....")


	time.sleep(5)
"""


	
def test(websiteBlocker):
    w=website.get()
    t1=time1.get()
    t2=time2.get()
    websiteBlocker.setWebsites(w)
    websiteBlocker.setTime(t1,t2)
    print(websiteBlocker.getWebsites())
    root.destroy()
    websiteBlocker.block()


websiteBlocker=websiteBlocker()
root=Tk()
root.title("Website Blocker")

website_name=Label(root,text="Website to block:")
website_name.grid(row=3,column=2)
website=Entry(root,bd=5)
website.grid(row=3,column=3)

time_label=Label(root,text="Time:PM")
time_label.grid(row=4,column=3)
time1=Entry(root,bd=5)
time1.grid(row=5,column=2)
time2=Entry(root,bd=5)
time2.grid(row=5,column=4)

enter=Button(root,text="Enter",command=(lambda:test(websiteBlocker)))
enter.grid(row=7,column=3)
root.mainloop()


