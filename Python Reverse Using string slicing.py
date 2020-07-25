#!/usr/bin/env python
# coding: utf-8

# In[2]:



# Python3 code to demonstrate working of 
# Reverse Slicing string  
# Using string slicing 
  
# initializing string  
test_str = "Python"
  
# printing original string  
print("The original string is : " + test_str) 
  
# initializing K  
K = 4
  
# Using string slicing 
# Reverse Slicing string  
res = test_str[(K-1)::-1] 
  
# printing result  
print("The reversed sliced string is : " + res) 

