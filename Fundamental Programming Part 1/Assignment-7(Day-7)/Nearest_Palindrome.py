'''
Created on Oct 5, 2019

@author: HITMAN

Problem Statement:

Write a python function, nearest_palindrome() which accepts a number 
and returns the nearest palindrome greater than the given number.

Solution:
'''
#lex_auth_01269443664174284882
def is_Palindrome(num):
    string=str(num)
    list1=[]
    list2=[]
    for i in string:
        list1.append(int(i))
        list2.append(int(i))
    list2.reverse()
    if list2 == list1:
        return True
    else:
        return False
        
    
def nearest_palindrome(number):
    num=number
    i=num+1
    while(True):
        if is_Palindrome(i)==True:
            return i
        else:
            i+=1
    
    

number=12300
print(nearest_palindrome(number)) 
