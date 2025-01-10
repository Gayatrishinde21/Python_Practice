import os
import datetime

''' command = "uptime" #load avearge 
command = "date" #date

def check_cpu(command):
    print(os.system(command))

check_cpu("uptime")

def check_date(command): #defining a function
    print(os.system(command))

check_date("date")  #calling a function

'''

def run_command(command):  #create function
    return os.system(command)
def show_date():
    return datetime.datetime.today()

#run_command("uptime")
#run_command("date")

today = show_date()
print(today)