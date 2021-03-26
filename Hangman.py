# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:15:07 2021

@author: cladz
"""
import random
import sys
import time


### Hangman

guess_fin = ""
guess_ltr = ""
list1 = ""
output = ""
trial = ""

count = 0
pts = 0
scan_times = 0

words = ["flashlight", "aircon", "monitor", "sinigang", "jollibee"]
sel_word = random.choice(words)
sel_word_visual = [] # list


for i in range(len(sel_word)):
    sel_word_visual.append("*") 

def hang_in_there_man(tries):
    global count 
    global guess_fin
    global guess_ltr   
    global lim
    global list1
    global output
    global pts
    global scan_times
    global sel_word
    global sel_word_visual
    global trial
    
    list1 = []
    list1[:0] = sel_word
    
    for loop in range(tries):
        time.sleep(2)
        print("///////////////////")
        print("Clue: %d letters" % len(sel_word))
        trial = "".join(sel_word_visual)
        print(trial)
        
        print("Tries left: %d" % tries)
        
        guess_fin = input("Do you wanna take a final guess? (No turning back! Only for pros.) [y/n]" + "\n")
        
        if (guess_fin == "y"):
            print("Clue: %d letters" % len(sel_word))
            guess_fin1 = input("Enter your FINAL guess: ")
            if guess_fin1 == sel_word:
                time.sleep(1.5)
                print("You're correct!")
                time.sleep(1.5)
                print("Lezgo!" +"\n\n")
                time.sleep(2)
                sys.exit("You win! Haaland to Barca TOOOOOT EL CAMP")
            else:
                time.sleep(1.5)
                print("NOOB!")
                time.sleep(1.5)
                print("Get out!")
                time.sleep(1.5)
                sys.exit("The correct word is '%s' LOL"  % sel_word + "\n")
            
        guess_ltr = input("Enter your letter guess: ")

        for i in list1: # check if right pick
            if guess_ltr == list1[scan_times]:
                sel_word_visual[scan_times] = guess_ltr
                count = count + 1             
                
            scan_times = scan_times + 1
        
        print("There are %d repetitions of '%s' in the word" % (count,guess_ltr) + "\n")    
        scan_times = 0 # reset scan_times to 0 every iteration
        count = 0   # reset count to 0 as well
        tries = tries - 1
        
    if tries == 0:
        print("Kriiiiiing")
        time.sleep(1.5)
        print("Loser!")
        time.sleep(1.5)
        print("Getto Outto!" + "\n")
        time.sleep(1.5)
        print("The correct word is '%s'" % sel_word)
        
    return sys.exit()

print("Welcome to Hangman!")
time.sleep(1.5)
username = input("Enter username: ")
entry_resp = ["pito't puting tupa ng ina mo, %s :)" % username, 'ha dabbing, %s' %username, 'malakas na ba yan, %s?' % username, '%s, nyenyenye' % username]
print("Here's your welcome messsage:" + "\n")
time.sleep(2) 
print(random.choice(entry_resp))
time.sleep(2)
tries = int(input("How many tries do you want? "))
print(input(hang_in_there_man(tries)))



# cant read 'i' guess in sinigang : goods na
# word visualization (if a guess letter is right, display it alongside ***) : goods
# is letter entered repeated? list guessed letters
# pointing system (lesser as number of tries decrease) (record in an excel file) (SQL?)
# get guess words from excel file column (column head = clue/category)
