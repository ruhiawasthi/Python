#!/usr/bin/env python
# coding: utf-8

# In[2]:


#string slicing
String = 'ASTRING'

#using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12 , -2)

print("String Slicing")
print(String[s1])
print(String[s2])
print(String[s3])

