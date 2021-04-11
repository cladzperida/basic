# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 03:12:40 2021

@author: user
"""

# F.L.A.M.E.S.
import numpy as np
import time

na_ctr = 0
match = 0
rep = 0
repeat_list1 = []
repeat_list2 = []


print("Crush ka ba ng crush mo?")
time.sleep(1)
print("Gaano kayo ka-match???")
time.sleep(0.5)
print("Welcome to F.L.A.M.E.S!")
time.sleep(1)

name1 = input("Enter name 1: ")
name1a = list(name1)
name1a.remove(" ")
name1a = [x.lower() for x in name1a]

name2 = input("Enter name 2: ")
name2a = list(name2)
name2a.remove(" ")
name2a = [x.lower() for x in name2a]

time.sleep(1)
print("The names you've entered are '%s' and '%s'. Yown bagay!!!" % (name1,name2))
time.sleep(0.5)

for x in name1a: # 'J'
    for y in name2a: # name 2
        if x == y: # matching element x from name1 to element y from flames 
            na_ctr = 0
            break
        else: # x != y
            na_ctr += 1
            if na_ctr == len(name2a):
                repeat_list1.append(x) # check later for repetition of leftover letters
                na_ctr = 0
                    # dapat hindi umuulit yung letter pag na-check na once na walang ka-match sa kabila

n1 = np.array(repeat_list1)
n1 = np.unique(n1) # find unique letters
n1 = n1.tolist()
n1_pts = len(n1)

for x in name2a:
    for y in name1a: # name 2
        if x == y: # matching element x from name1 to element y from flames 
            na_ctr = 0
            break
        else: # x != y
            na_ctr += 1
            if na_ctr == len(name1a):
                repeat_list2.append(x) # check later for repetition of leftover letters
                na_ctr = 0
                
n2 = np.array(repeat_list2)        
n2 = np.unique(n2) # find unique letters
n2 = n2.tolist()
n2_pts = len(n2)

print("And your F.L.A.M.E.S. result is...")
time.sleep(1)

match = n1_pts + n2_pts

print("\n")

if (match == 1) or (match - 6 == 1) or (match - 6*2 == 1):
    print("F as in Friends! (or F's in the chat) with %d matches" % match)
if (match == 2) or (match - 6 == 2) or (match - 6*2 == 2):
    print("L as in Lovers! Yown! with %d matches" % match)
if (match == 3) or (match - 6 == 3) or (match - 6*2 == 3):
    print("A as in Angery! Grrrr! with %d matches" % match) 
if (match == 4) or (match - 6 == 4) or (match - 6*2 == 4):
    print("M as in Marriage! Kelan kasal?! with %d matches" % match)
if (match == 5) or (match - 6 == 5) or (match - 6*2 == 5):
    print("E as in Enemies! Sapakan! with %d matches" % match)
if (match == 6) or (match - 6 == 6) or (match - 6*2 == 6):
    print("S as in Soulmates! Yieeee xDDDD with %d matches" % match)
