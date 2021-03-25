# Random Password Generator
"""
Created on Wed Mar 24 17:01:14 2021

@author: cladz
"""
import string
import time
import random
import sys

letters = list(string.ascii_letters)
num = ['0','1','2','3','4','5','6','7','8','9']
char_letter = ['!','@','#','$','%', '^','&','*','(',')','-','+'] + letters
result = ""

def random_pw(length):
    global letters
    global num
    global result
    for ctr in range(length):
        if(ctr % 2) == 0: # even; select from letters
            le = random.choice(char_letter)
#            ch = random.choice(char)
            result = result + le
            continue
        else:
            nu = random.choice(num)
            result = result + nu
            continue
    
    time.sleep(2)
    print("Your %d-digit-long randomly generated password is: %s" % (length,result))
 
    return sys.exit()

print("Welcome to Random Password Generator!" + "\n")
time.sleep(2)
length = int(input("How long is the password needed? "))

print(input(random_pw(length)))
