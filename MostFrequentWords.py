# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 00:52:02 2021

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 05:22:02 2021

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string
import sys
# Word Counter & Visualizer

freq = []
ctr = 0
error = 0
scan = 0
# locate every word
# each space is a mark that a word has ended
## ^ use split perhaps? --- check
def word_ctr_plt(txt):
    global scan
    global ctr
    global df
    global freq
    global freq1
    global uniq_msg
    global updated_lst
    global raw_msg
    global word
    global word_freq
    
    for char in string.punctuation:
        txt = txt.replace(char, "")

    raw_msg = txt.split(" ") # u must remove the commas, dots, parenthesis, etc. --- not quite done
    # for the last word of line 1 and first word of line 2, separate them:
    # for words like "I'll" which can be read (without symbols) as "Ill", fix this:
    raw_msg = [x.lower() for x in raw_msg]
    uniq_msg = np.array(raw_msg)
    uniq_msg = uniq_msg.tolist()
    uniq_msg = np.unique(uniq_msg)
    uniq_msg = uniq_msg.tolist()
    # count number of words/objects in list

    for i in range(len(uniq_msg)):
        freq.append(0)   
 
    for a in uniq_msg:
        for b in raw_msg:
            if a == b:
                freq[ctr] += 1
                scan += 1
                if scan == len(raw_msg):
                    ctr += 1
                    scan = 0
            else:
                scan += 1
                if scan == len(raw_msg):
                    ctr += 1
                    scan = 0
    # then, get most repeated words                         
    # using bar graph, plot the top 5 most repeated words, if there is any
    #freq1 = freq
    df = pd.DataFrame(freq,index= uniq_msg, columns=['frequency']) 
    df = df.sort_values(by='frequency', ascending=False)
    word_freq = df['frequency'].tolist()
    word = df.index.tolist()
    
    word = word[:10]
    word_freq = word_freq[:10]
    
    plt.bar(word,word_freq)
    plt.show()
    return sys.exit()

txt = input("Enter text to be analyzed: ")
print(input(word_ctr_plt(txt)))