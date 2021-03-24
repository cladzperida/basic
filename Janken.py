# Rock, Papers, Scissors
"""
Created on Tue Mar 23 20:44:22 2021

@author: cladz
"""

import random
import time

pt_cpu = 0
pt_user = 0
select = ['a', 'b', 'c'] # choices basket

def janken(rounds):
    global pt_cpu
    global pt_user 

    for ctr in range(rounds):
        print("\n" + "Current score: You(%d) vs CPU(%d)" % (pt_user,pt_cpu))
        pk_user = input("Enter pick: ")
        pk_cpu = random.choice(select)   # pk_cpu = random choice
        print("CPU Pick: %s" % pk_cpu)

        if (pk_user == 'a' and pk_cpu == 'b') or (pk_user == 'b' and pk_cpu == 'c') or (pk_user == 'c' and pk_cpu == 'a'):
            pt_cpu += 1
            continue
        if (pk_user == 'a' and pk_cpu == 'c') or (pk_user == 'b' and pk_cpu == 'a') or (pk_user == 'c' and pk_cpu == 'b'):
            pt_user += 1
            continue
        else:
            print("Yikes same picks lol")
            
    if(pt_user > pt_cpu):
            print("\n" + "-*-*-*-*-*-*-*-*-*-*")  
            print("\n"+ "You are the winner with %d points vs %d CPU points!" % (pt_user,pt_cpu))
            print("Congrats! Here's the response of your opponent: ")
            lose_cpu = ["Sorry na master...", "Natagpuan kita <3", "*leaves convo*", "Sorry ganito lang ako..."]
            lose_cpu_resp = random.choice(lose_cpu)
            time.sleep(3)
            print(lose_cpu_resp.upper())
    elif (pt_user < pt_cpu):
            print("\n" + "-*-*-*-*-*-*-*-*-*-*")
            print("\n" + "You are NOT the winner with %d vs %d CPU points!" % (pt_user,pt_cpu))
            print("Oh no you're a loser! Here's the response of your opponent: ")
            win_cpu = ["Tawagin mo kong master", "Sayaw ka with feelings", "Bilhan mo ko 1 bitcoin!"]
            win_cpu_resp = random.choice(win_cpu)
            time.sleep(3)
            print(win_cpu_resp.upper())
    else: 
            print("-*-*-*-*-*-*-*-*-*-*")    
            print("\n" + "Draw talaga eh HAHAHAHA you with %d vs %d CPU!" % (pt_user,pt_cpu))
            print("Wengkwonk! Here's the response of your opponent: ")
            time.sleep(3)
            draw_cpu = ["Rematch?", "Sayaw na lang tayong2 dalawa", "Gusto ko ako lang gustooo"]
            draw_cpu_resp = random.choice(draw_cpu)
            print(draw_cpu_resp.upper())
            
    return

print("Welcome to Janken!" + "\n")
rounds = int(input("How many rounds do you want to play? "))

message_usr = input("Do you have any message to your opponent? " + "\n")
print("\n" + "Savage! Here's the response of your opponent: ")
message_cpu = ["GG na agad di pastart","I'll defeat you alive","Oh tawa pa sige","Chrysler Lee chinese", "Oh lew-hood", "'%s' your face!" % message_usr]
ms_cpu = random.choice(message_cpu)
time.sleep(1.5)
print(ms_cpu.upper() + "\n")
time.sleep(3)
print("Type 'a' if ROCK")
print("Type 'b' if PAPER")
print("Type 'c' if SCISSORS")

print(input(janken(rounds)))