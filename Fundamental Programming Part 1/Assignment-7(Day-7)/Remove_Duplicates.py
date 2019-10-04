'''
Created on Oct 5, 2019

@author: HITMAN

Problem Statement:
Write a python function, remove_duplicates() which accepts a string
and removes all duplicate characters from the given string and 
return it.

#lex_auth_01269446319507046499
'''
Solution:

def remove_duplicates(value):
    
    list=[]
    list1=[]
    for i in value:
        list.append(i)
    for i in list:
        if i not in list1:
            list1.append(i)
    
    string=''
    for i in list1:
        string+=i
    return string

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
