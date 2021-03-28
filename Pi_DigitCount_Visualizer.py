# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 02:40:39 2021

@author: user
"""

# Pi Digit Counter (w/ visuals)

import matplotlib.pyplot as plt
import pandas as pd
import time

digit = ['0','1','2','3','4','5','6','7','8','9']
tot_count = 0

print("Welcome to Pi Digit Counter Visualizer!")
time.sleep(1.5)
total = int(input("How many digits of pi do you want? "))

pi = pd.read_excel("pi_digit.xlsx", sheet_name=0, nrows = total) # can also index sheet by name or fetch all sheets
pi1 = pi['digits'].tolist()

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0 

for i in pi1:
    if tot_count < len(pi1):    # clearing graph every iteration
        plt.cla()
    freq = [count0,count1,count2,count3,count4,count5,count6,count7,count8,count9]
    plt.title('Pi Digit Counter XD')
    plt.xlabel('digits')
    plt.ylabel('frequency')  
    barlist = plt.bar(digit,freq)
    
    
    if i == 0:
        count0 += 1
        # if (count0 >= 50) and (count0 <= 100):
        #     barlist[0].set_color('r')
        # if (count0 > 100) and (count0 <= 500):
        #     barlist[0].set_color('g')
    if i == 1:
        count1 += 1
        # if (count1 >= 50) and (count1 <= 100):
        #     barlist[1].set_color('r')
        # if (count1 > 100) and (count1 <= 500):
        #     barlist[1].set_color('g')
    if i == 2:
        count2 += 1
        # if (count2 >= 50) and (count2 <= 100):
        #     barlist[2].set_color('r')
        # if (count2 > 100) and (count2 <= 500):
        #     barlist[2].set_color('g')
    if i == 3:
        count3 += 1
        # if (count3 >= 2) and (count3 <= 100):
        #     barlist[3].set_color('r')
        # if (count3 > 100) and (count3 <= 500):
        #     barlist[3].set_color('g')
    if i == 4:
        count4 += 1
        # if (count4 >= 50) and (count4 <= 100):
        #     barlist[4].set_color('r')
        # if (count4 > 100) and (count4 <= 500):
        #     barlist[4].set_color('g')
    if i == 5:
        count5 += 1
        # if (count5 >= 50) and (count5 <= 100):
        #     barlist[5].set_color('r')
        # if (count5 > 100) and (count5 <= 500):
        #     barlist[5].set_color('g')
    if i == 6:
        count6 += 1
        # if (count6 >= 50) and (count6 <= 100):
        #     barlist[6].set_color('r')
        # if (count6 > 100) and (count6 <= 500):
        #     barlist[6].set_color('g')
    if i == 7:
        count7 += 1
        # if (count7 >= 50) and (count7 <= 100):
        #     barlist[7].set_color('r')
        # if (count7 > 100) and (count7 <= 500):
        #     barlist[7].set_color('g')
    if i == 8:
        count8 += 1
        # if (count8 >= 50) and (count8 <= 100):
        #     barlist[8].set_color('r')
        # if (count8 > 100) and (count8 <= 500):
        #     barlist[8].set_color('g')
    if i == 9:
        count9 += 1
        # if (count9 >= 50) and (count9 <= 100):
        #     barlist[9].set_color('r')
        # if (count9 > 100) and (count9 <= 500):
        #     barlist[9].set_color('g')
    tot_count += 1
    plt.pause(0.00001)


    
    
    
    
    
    
    