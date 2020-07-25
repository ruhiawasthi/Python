#!/usr/bin/env python
# coding: utf-8

# In[5]:



# Python3 code to demonstrate working of 
# Reverse Slicing string  
# Using join() + reversed() 
  
# initializing string  
test_str = "Python"
  
# printing original string  
print("The original string is : " + test_str) 
  
# initializing K  
K = 4
  
# Using join() + reversed() 
# Reverse Slicing string  
res = ''.join(reversed(test_str[0:K])) 
  
# printing result  
print("The reversed sliced string is : " + res) 

