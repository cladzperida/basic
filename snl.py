# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 23:13:30 2021

@author: user
"""

import numpy as np
import pandas as pd
import random as rd
import sys
import time

def xy_checker(ctr):
    global hld
    global usr1
    
    # if snake, find sn head
    if usr1 in sn_heads:
        time.sleep(1)
        print("SNAKES!!!")
        for i in sn_heads:
            if usr1 == i:
                hld += 1
                break
            else:
                hld += 1
        usr1 = sn_tails[hld-1] # new location
        hld = 0
        print("The new coordinate is:", usr1)
    # if ladder, find ld tail
    if usr1 in ld_tails:
        time.sleep(1)
        print("LADDERS!!! GOING UP!")
        for i in ld_tails:
            if usr1 == i:
                hld += 1
            else:
                hld += 1
        usr1 = ld_heads[hld-1] # new location
        hld = 0
        print("The new coordinate is:", usr1)
    hld = 0
    return # if none, go back to origin loop

hld = 0 
sn_xy = []
ld_xy = []
sn_heads = []
sn_tails = []
ld_heads = []
ld_tails = []
sn_t_y_AAA_uniq = []
sn_t_y_uniq = []
ctr = 3
i = 10
snl_map = np.zeros(shape=(i,i)) # map creation
#snl_map = -100*snl_map

sn_h_locs = [1,3,5,7,9] # snake head row locs 
sn_t_locs = [0,2,4,6,8] # snake tail row locs    
    
df = pd.DataFrame({'sn_head':sn_h_locs,'sn_tail':sn_t_locs})
df = df.sort_values(['sn_head','sn_tail'], ascending=False)
df_tail = pd.DataFrame({'ld_head':sn_h_locs,'ld_tail':sn_t_locs})
df_tail = df_tail.sort_values(['ld_head','ld_tail'], ascending=False)  

# generate 3 snakes in total
while(ctr > 0):
        # generate snake head
        sn_t_y = rd.choice(range(5)) # index selectors
        if sn_t_y == 0:
            sn_t_y = 4
            sn_h_y = rd.choice(range(sn_t_y))
        else:
            sn_h_y = rd.choice(range(sn_t_y)) 
        # select sn_head value here (y-component)
        sn_t_y = df.loc[[sn_t_y],['sn_head']]
        sn_t_y = sn_t_y['sn_head'].tolist()
        sn_h_y = df.loc[[sn_h_y],['sn_tail']]
        sn_h_y = sn_h_y['sn_tail'].tolist()
        sn_t_y = sn_t_y[0]
        sn_h_y = sn_h_y[0]
        # now get columns for x-coordinate
        sn_t_x = rd.choice(range(10))
        sn_h_x = rd.choice(range(10))
        # uniq_xy.append([sn_t_y,sn_t_x])
        # uniq_xy.append([sn_h_y,sn_h_x])
#        [sn_t_y,sn_t_x] = [0,0] # trial
        if [sn_h_y,sn_h_x] == [0,0]:
            [sn_h_y,sn_h_x] = [sn_t_y + 1,sn_t_x - 1] 
        # check here if all coordinates are unique (below this) (wala pa)
        # sn_xy.append([[sn_t_y,sn_t_x],[sn_h_y,sn_h_x]]) # snake coordinates
        sn_xy.append([[sn_h_y,sn_h_x],[sn_t_y,sn_t_x]]) # snake coordinates
        sn_heads.append([sn_h_y,sn_h_x]) # snake heads
        sn_tails.append([sn_t_y,sn_t_x])
    
        ctr -= 1
        if ctr == 0:
            break
        
sn_df = pd.DataFrame({'sn_head':sn_heads,'sn_tail':sn_tails})

# write the snake coordinates into the matrix snl_map
for i in range(3): # 0
    for j in range(2): # 0
        snl_map[sn_xy[i][j][0],sn_xy[i][j][1]] = -(i+1)  # only one coordinate per snake

# snakes generated

# generate 3 ladders
ctr = 3
while(ctr > 0):
        # generate snake head
        ld_t_y = rd.choice(range(5)) # index selectors
        if ld_t_y == 0:
            ld_h_y = 0
        else:
            ld_h_y = rd.choice(range(ld_t_y)) 
        # select sn_head value here (y-component)
        ld_t_y = df_tail.loc[[ld_t_y],['ld_head']]
        ld_t_y = ld_t_y['ld_head'].tolist()
        ld_h_y = df_tail.loc[[ld_h_y],['ld_tail']]
        ld_h_y = ld_h_y['ld_tail'].tolist()
        ld_t_y = ld_t_y[0]
        ld_h_y = ld_h_y[0]
        # now get columns for x-coordinate
        ld_t_x = rd.choice(range(10))
        ld_h_x = rd.choice(range(10))
        if [ld_t_y,ld_t_x] == [9,0]:
            [ld_t_y,ld_t_x] = [ld_h_y - 1,ld_h_x + 1] 
        # check here if all coordinates are unique (below this) (wala pa)
        ld_xy.append([[ld_h_y,ld_h_x],[ld_t_y,ld_t_x]]) # ladder coordinates
        ld_tails.append([ld_t_y,ld_t_x]) # ladder tails
        ld_heads.append([ld_h_y,ld_h_x])

        ctr -= 1
        if ctr == 0:
            break

ld_df = pd.DataFrame({'ld_head':ld_heads,'ld_tail':ld_tails})

# write the ladder coordinates into the matrix snl_map
for i in range(3): # 0
    for j in range(2): # 0
        snl_map[ld_xy[i][j][0],ld_xy[i][j][1]] = i+1  # only one coordinate per snake
        
# snakes and ladders are all generated
# wala pa tong unique coordinates for snakes vs ladders, 
# re-run na lang hanggang maging unique for now

### gameplay begins
ctr = 1 # game validity checker
# user 1
usr1 = [0,0]
usr1[1] = 0 # initial position
usr1[0] = 9
usr1 = [usr1[0],usr1[1]] 

# dice creator
dice_choice = list(range(7))
dice_choice.remove(0)

# movement along matrix
# while loop here

# create functions for odd rows and even rows

while ctr > 0:
    # prompt for a dice roll
    
    print("The current location is:" , usr1)
    print("\n")
#    usr1 = sn_xy[1][0] # test case when usr @ snake head
    snl_map[usr1[0]][usr1[1]] = 5
    print(snl_map)
    print("\n")
    dice = input("Roll the dice? (y/n)")
    if dice == "y":
        time.sleep(0.5)
        dice = rd.choice(dice_choice)
    print(dice)
# if odd, to right (add)
    if usr1[0] % 2 != 0: # odd row
        usr1[1] += dice
        if usr1[1] > 9: # out of bounds; move to higher row
            usr1[1] -= 9 # new coordinates
            usr1[0] -= 1
        # new xy
        # check if there is a snake/ladder at this xy
        # create function xy_checker
        input(xy_checker(ctr))
# if even, to left (sub)
    else: # even row
        usr1[1] -= dice
        if usr1 == [0,0]:
            print("You win!")
            snl_map[usr1[0]][usr1[1]] = 100
            sys.exit()
        if (usr1[0] == 0) and (usr1[1] < 0): # exceeding map max; restart
            usr1 = [9,0] # original xy
            continue
        if usr1[1] < 0: # out of bounds; move to higher row
            usr1[1] = -usr1[1] # new coordinates
            usr1[0] -= 1
        input(xy_checker(ctr))

