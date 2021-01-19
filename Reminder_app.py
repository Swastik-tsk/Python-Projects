
import notify2 														
import getpass														
import os
import schedule														
import time

def water_notification():
	print("Drink Water!!!")								
	name=getpass.getuser()										
	message="Hello highness"+name
	notify2.init(message)
	n = notify2.Notification(message+" It is time for you to hydrate yourself")
	task="espeak "+"'"+message +"please drink water"+"'" +" -s 150"
	os.system(task)														
	n.set_urgency(notify2.URGENCY_NORMAL)					
	n.set_timeout(100) 
	n.show()													

def wish(): 			
	pwd=os.getcwd()							    					
	name=getpass.getuser()										
	current_time=time.localtime()
	if current_time[3] < 12 :
		message=" Good Morining "+name
		task="espeak "+"'"+message +" Have a nice day"
	elif current_time[3] in range(12,18):
		message=" Good Afternoon "+name
		task="espeak "+"'"+message +" Hope you are fine"	
	else :	
		message=" Good Evening "+name
		task="espeak "+"'"+message +" Have a pleasant evening "
	os.system(task)															

def take_a_break():
	print("Take a break")							
	name=getpass.getuser()										
	message="Hello "+name
	notify2.init(message)
	n = notify2.Notification(message+" Take a break....")
	task="espeak "+"'"+message +"I think you need to take a break"+"'" +" -s 150"
	os.system(task)															
	n.set_urgency(notify2.URGENCY_NORMAL)							
	n.set_timeout(100)												 
	n.show()												
	
if __name__=="__main__":											
	wish()
	print("Hey there....")
	print("This is a simple reminder app in python!!!")
	# we schedule for every one hour to make a notification related to drink water.
	schedule.every().hour.do(water_notification)					    
	# for every 35 minutes we schedule the user to take a break
	schedule.every(35).minutes.do(take_a_break					    
	schedule.every(480).minutes.do(wish)					    	
	while True:
		schedule.run_pending()
		time.sleep(1)	