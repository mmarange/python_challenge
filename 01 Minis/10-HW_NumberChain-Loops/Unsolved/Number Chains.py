# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:49:30 2020

@author: dell
"""
response = "y"
z = 0
# request input
while response == "y":

    n = int(input("How many numbers?"))
  
# loop to print numbers starting with 0
    for x in range(z+n+1):
        print(x)
    
    response = input("Would you like to continue (y/n)")        
    z=z+n
    #response = input("Would you like to continue (y/n)")  
