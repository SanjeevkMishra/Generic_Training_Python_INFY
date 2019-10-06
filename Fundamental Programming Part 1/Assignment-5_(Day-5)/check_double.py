'''
Created on Oct 6, 2019

@author: HITMAN

Problem Statement:

Write a python function, check_double(number) which accepts a whole 
number and returns True if it satisfies the given conditions.
The number and its double should have exactly the same number of 
digits.

Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain 
exactly the same digits, but in a different order.

Solution:
'''
#lex_auth_01269441810970214471

def check_double(number):
    #Remove pass and write your logic here
    n1=number
    n2=2*number
    string1=str(n1)
    string2=str(n2)
    if len(string1)!=len(string2):
        return False
    
    list1=[]
    list2=[]
    for i in string1:
        list1.append(int(i))
    for i in string2:
        list2.append(int(i))
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False

#Provide different values for number and test your program
print(check_double(125874))
