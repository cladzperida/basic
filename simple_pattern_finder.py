# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 02:48:08 2021

@author: user
"""

# Simple Pattern Finder

import sys
import time

num_list = []
diff_list = []
quo_list = []
ctr = 0
cd = 0
diff = 0

# Common Difference
def patt_find_cd(dig):
#    global num_list
    global cd
    global ctr
    global data
    global diff
#    global dig
    global diff_ave
    global diff_mode
    global diff_l1
    # soon, ask how many digits to input
    # for now, make it 5 = dig
    
#    print("Enter %d digits to be analyzed: " + "\n")
    while (dig > 0):
        num = int(input("Enter digit:"))
        num_list.append(num)
        dig = dig - 1
    print("Your list is: " , num_list)
    time.sleep(1)
    # analysis part starts here
    # test first if there is a common difference
    # create new list for differences?
    dig = 5 # xD
    while (dig > 0):
        diff = num_list[ctr + 1] - num_list[ctr]
        diff_list.append(diff)
        ctr += 1
        if ctr == len(num_list) - 1:
            break # break out of while loop
        dig -= 1
    # check difference list if succeeding elements are equal...
    dig = len(diff_list)
    ctr = 0
    # get average of diff_list
    diff_ave = sum(diff_list)/dig # average
    if diff_ave == diff_list[0]:
        cd = diff_ave # assign it as the common diff (cd)
        print("The list has a common difference!")
        time.sleep(1)
    else:
        print(input(patt_find_cr(dig))) # check if there is common ratio
    # now for extrapolation...
    dig = len(num_list)
    ctr = dig
    for i in range(dig):
        diff_l1 = num_list[0] + ctr*cd
        num_list.append(int(diff_l1))
        ctr = len(num_list) # new length of num_list
    print("The next digits on the list are: ")
    time.sleep(2.5)
    print(num_list[dig:])
    time.sleep(4)
    return sys.exit("\n\n"+"Goodbye!!!")

# Common Ratio
def patt_find_cr(dig): # common ratio
    global cr
    global quo    
    global quo_list
    global quo_l1
#    global dig   
    global ctr 
    # divide i+1'th element / i'th element
    dig = len(num_list)
    while(dig > 0):
        quo = num_list[ctr + 1] / num_list[ctr]
        quo_list.append(quo)
        ctr += 1
        if ctr == len(num_list) - 1:
            break # break out of while loop
        dig -= 1
    dig = len(quo_list)
    ctr = 0
    # get average of diff_list
    quo_ave = sum(quo_list)/dig # average
    if quo_ave == quo_list[0]:
        cr = quo_ave # assign it as the common diff (cd)
        print("The list has a common ratio!")
        time.sleep(1)
    else:
        print("LMAO your list doesn't have either a) common diff or b) common ratio.")
        time.sleep(1)
        print("Get back here for further developments...")
        sys.exit("Goodbye novice!")
    dig = len(num_list)
    ctr = dig
    for i in range(dig):
        quo_l1 = num_list[0] * cr ** ctr
        num_list.append(int(quo_l1))
        ctr = len(num_list) # new length of num_list
    print("The next digits on the list are: ")
    time.sleep(2.5)
    print(num_list[dig:])
    time.sleep(4)
        
    # complete for entire list -> store into new rat_list
    # get average of that rat_list
    # if ave(rat_list) = rat_list[0], then there is common ratio
    return sys.exit("\n\n" + "Goodbye!!!")

print("Welcome to Simple Pattern Finder!")
time.sleep(2)
# How many digits do u want?
dig1 = int(input("Enter how many digits do you want to extrapolate: "))
dig = 5 # xD
print(input(patt_find_cd(dig)))