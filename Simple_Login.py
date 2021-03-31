# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:09:33 2021

@author: user
"""

# Simple Log-in
import pandas as pd
import sys
import time
from xlwt import Workbook

username = ""
password = ""
name_list1 = []
pw_list1 = []
rb = ""
sheet1 = ""
holder = 0
long = 0
ctr = 0
tries = 5

def returning(comeback): # returning customer
    global username
    global password
    global rb
    global sheet1
    global long
    global name_list
    global pw_list
    global ctr
    global registrar
    global tries
    global holder
    
    print("Welcome back, old user!")
    time.sleep(2)
    username = input("Enter your username: ")
    # check if recurring
    for i in name_list:
        if i == username:
            print("Welcome back, %s!" %username)
            time.sleep(1)
            for i in range(tries):
                password = input("Enter your password: ")
                if password == pw_list[holder]:
                    time.sleep(2)
                    print("welcome back, %s!!!" % username)
                    time.sleep(1)
                    sys.exit()
                tries = tries - 1
                time.sleep(1)
                print("WROOOOOONG!")
                time.sleep(0.5)
                if tries < 3:
                    print("Hmmmm u a sketchy person...")
                time.sleep(0.5)
                print("Tries left: %d" % tries)
                if tries == 0:
                    sys.exit("Nice try, hackerman!")
        holder += 1    
    print("...hmmm, you're new")
    time.sleep(2)
    registrar = input("Want to create a new account instead? (y/n) ")
    if registrar == 'y':
        print(input(new(registrar)))
    else:
        print(input(returning(registrar)))

    return sys.exit()

def new(comeback): # new customer
    global username
    global password
    global rb
    global sheet1
    global long
    global name_list
    global pw_list
    global ctr
    
    print("Welcome new user!")
    time.sleep(2)
    username = input("Enter your username: ")
    # check dataframe if umulit na
    for i in name_list:
        if i == username:
            print("That's already registered!")
            sys.exit()
    name_list.append(username)          
    password = input("Enter your password: ")
    pw_list.append(password)
    long = len(name_list) # also equal to len(pw_list)
    
    wb = Workbook()
    sheet1 = wb.add_sheet('Login') #create  
    sheet1.write(0, 0, 'username')
    sheet1.write(0, 1, 'password')
    
    for i in range(long):
         sheet1.write(ctr + 1, 0, name_list[ctr])
         sheet1.write(ctr + 1, 1, pw_list[ctr])
         ctr += 1
    wb.save('Login_New.xls') 
    
    return sys.exit()

df = pd.read_excel("Login_New.xls", sheet_name=0)
name_list = df['username'].tolist()
pw_list = df['password'].tolist()

comeback = input("Returning user? [y/n] ")
if comeback == 'y':
    print(input(returning(comeback)))
else:
    print(input(new(comeback)))