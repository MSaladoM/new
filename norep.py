# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:49:46 2022

@author: Mariana Salado Mejía
This program reads a string S (of any length) and identifies if S was formed by 
concatenating a string T with itself one or more times. 
Finally, the program prints the smallest T from which S can be obtained by repetition.
The program also computes the length of the string and the number of times the 
string T is repeated.
ESTE ES EL CAMBIO EN EL CÓDIGO

"""
class NoRep:
    
    #Retrieve the smallest string T from which S can be obtained by repetition 
    #Input: String 's'
    #Output: String 'T'
    def norepf(self,s):
        factors1 = []
        #This for-loop obtains all the divisors of the string lenght
        for i in range(1,len(s)+1):
            if len(s)%(i) == 0:
                factors1.append(i)
        #The divisors are used as marks to slice the strings and compare 
        #the first slice with the second slice and the first slice with the last slice.
        #If the slices are equal, then the corresponding string in the slice is 
        #the smallest string T
        for i in factors1:
            if (s[0:i]==s[len(s)-i:] and s[0:i]==s[i:2*i]):
                m=i
                T=s[0:m]
                break
            else:
                T=s
        return T

    #Gives the length of the smallest T
    #Input: String 's'
    #Output: Integer 'lengt'
    def lengt(self,s):
        lengt=len(self.norepf(s))
        return lengt
    
    #Gives the number of times the string T is repeated
    #Input: String 's'
    #Output: Integer 'times'
    def times(self,s):
        times=int(len(s)/len(self.norepf(s)))
        return times



#-------------------------------------------------------------

if __name__ == '__main__':

	#Instantiate the class NoRep
	rn=NoRep()
	#Use the function norepf to find the string T
	print('Please input the string: ')
	x=input()
	not_rnw=rn.norepf(x)
	
	print(not_rnw)

