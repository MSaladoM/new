# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:55:37 2022

@author: Mariana Salado

This program call norep with different input values and compare norep's 
output against expected results. 
"""

#Import the necessary libraries and the class from norep
from norep import NoRep
import random 


charmax=5 #Maximum number of characters of the initial word

characters=['a','b','c','d','e','f','g','h',
            'i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z'] #Characters that can be used in the initial word generation


word=[]
nrand= random.randrange(1,charmax+1)

#This for-loop creates the initial word equivalent to the string T
for i in range(nrand):
    rand_idx = random.randrange(len(characters))
    word.append(characters[rand_idx]) #The characters are chosen randomly and added to a list
    new_word=''.join(word)  #The list is converted into a string 

rep_new_word=new_word*random.randrange(1,10)#Repeat the initial word n times given by a random number

#Instantiate the class NoRep
rn=NoRep()
#Use the function norepf to find the string T
not_rnw=rn.norepf(rep_new_word)


#Comparison between the length of the new word and the length of the string T given by
#the function norepf. If the lengths are the same, then the program works well, 
#else the program doesn't work well
if len(not_rnw)==len(new_word):
    print('The program works well')
else:
    print('The program doesn\'t work well')
    print('T calculated by program:',not_rnw)
    print('T given by test:',new_word)