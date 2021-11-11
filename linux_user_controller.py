#ignore error on line 23, i wrote this code in spyder and the code is meant to run on the unbuntu terminal, not here.
import pwd, grp
import sys
import subprocess
from subprocess import Popen, PIPE
import time as t
import getpass

username = ''
admin_usernames = ''
list_of_admin_users = []
list_of_users_admin_version = []
list_of_Wanted_users = []
list_of_Users = []


def list_of_wanted_users():
	global username
	username = username.split(",")
	e = []
	with Popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1", shell=True, stdout=PIPE, universal_newlines=True) as process:
    	for line in process.stdout:
        	e.append(line)
	e = [y.replace('\n', '') for y in e]
	for u in username:    
    	if u in e:
            	list_of_Wanted_users.append(u)
    	elif u not in e:
            	make = input('{0} is not a user in this computer, would you like to make {0} a user?(yes or no):'.format(u))
            	if make.lower() == 'yes':
                	r = subprocess.run('sudo useradd {0}'.format(u),shell=True)
                	if r.returncode == 0:
                     	list_of_Wanted_users.append(u)
                     	password = input('{0} is now a user, do you want to give it a password?(yes or no):'.format(u))
                     	if password.lower() == 'yes':
                        	word = subprocess.run('sudo passwd {0}'.format(u),shell=True)
                        	if word.returncode == 0:
                            	print('{0} now has a password'.format(u))
            	elif make.lower() == 'no':
                	pass
               	 
	list_of_users()
           	 
def list_of_users():
	e = []
	with Popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1", shell=True, stdout=PIPE, universal_newlines=True) as process:
    	for line in process.stdout:
        	e.append(line)
    	global list_of_Users
    	list_of_Users= [y.replace('\n', '') for y in e]
	delete_users()


def delete_users():
	for x in list_of_Users:
    	if x not in list_of_Wanted_users:
        	output = subprocess.run('sudo userdel -f {0}{1}'.format(' ',x),shell=True)
        	if output.returncode == 0:
            	print("User successfully deleted with given credentials")
            	t.sleep(2)

	done = subprocess.run(["cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1"], shell=True)
    
    
# this is the start of the removing admin right portion of the code
    
def list_of_wanted_admin_users():
	global admin_usernames
	admin_usernames = admin_usernames.split(",")
	i = []
	with Popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1", shell=True, stdout=PIPE, universal_newlines=True) as process:
    	for line in process.stdout:
        	i.append(line)
	i = [y.replace('\n', '') for y in i]
	e = []
	with Popen("getent group sudo | cut -d: -f4", shell=True, stdout=PIPE, universal_newlines=True) as process:
    	for line in process.stdout:
        	e.append(line)
	e = [y.replace('\n', '') for y in e]
	e = str(e)
	e = e.replace('[', '')
	e = e.replace(']', '')
	e = e.replace("'", '')
	e = e.split(',')
	for u in admin_usernames:    
    	if u in e:
            	list_of_admin_users.append(u)
    	elif u not in i:
        	make = input('{0} is not a user in this computer, would you like to make {0} a user?(yes or no):'.format(u))
        	if make.lower() == 'yes':
            	r = subprocess.run('sudo useradd {0}'.format(u),shell=True)
            	if r.returncode == 0:
                	admin_usernames.append(u)
                	i.append(u)
                	password = input('{0} is now a user, do you want to give it a password?(yes or no):'.format(u))
                	if password.lower() == 'yes':
                        	word = subprocess.run('sudo passwd {0}'.format(u),shell=True)
                        	if word.returncode == 0:
                            	print('{0} now has a password'.format(u))
        	elif make.lower() == 'no':
            	pass
    	elif u not in e and u in i:
            	Amake = input('{0} is not a admin on this computer, would you like to make {0} a admin?(yes or no):'.format(u))
            	if Amake.lower() == 'yes':
                	r = subprocess.run('sudo usermod -aG sudo {0}'.format(u),shell=True)
                	if r.returncode == 0:
                  	print('{0} is now an admin'.format(u))  
                  	list_of_admin_users.append(u)

            	elif Amake.lower() == 'no':
                	pass
	list_of_all_users()
    
    
def list_of_all_users():
	e = []
	with Popen("getent group sudo | cut -d: -f4", shell=True, stdout=PIPE, universal_newlines=True) as process:
    	for line in process.stdout:
        	e.append(line)
	e = [y.replace('\n', '') for y in e]
	e = str(e)
	e = e.replace('[', '')
	e = e.replace(']', '')
	e = e.replace("'", '')
	e = e.split(',')
	global list_of_users_admin_version
	list_of_users_admin_version = e
	remove_admin()

    
    
    
def remove_admin():
	for x in list_of_users_admin_version:
    	if x not in list_of_admin_users:
        	output = subprocess.run('sudo deluser {0} sudo'.format(x),shell=True)
        	if output.returncode == 0:
            	t.sleep(2)

	done = subprocess.run(["getent group sudo | cut -d: -f4"], shell=True)

which_one = input('Do you want to manage users or change their admin settings?(put either admin or users):')
which_one = which_one.lower()
if which_one == 'users':
	username = input("Enter Usernames that are suppose to be on this machine: ")
	if username == '':
    	print('cant be blank')
    	sys.exit()
	list_of_wanted_users()
elif which_one == 'admin':
	admin_usernames = input("Enter Usernames that are suppose to be admin on this machine: ")
	if admin_usernames == '':
    	print('cant be blank')
    	sys.exit()
	list_of_wanted_admin_users()

