'''
Created on Oct 6, 2019

@author: HITMAN

Problem Statement:
Consider sample data as follows: sample_data=range(1,11)

Create two functions: odd() and even()
The function even() returns a list of all the even numbers from 
sample_data The function odd() returns a list of all the odd numbers
from sample_data

Create a function sum_of_numbers() which will accept the sample data 
and/or a function. If a function is not passed, the sum_of_numbers()
should return the sum of all the numbers from sample_data If a function
is passed, the sum_of_numbers() should return the sum of numbers 
returned from the function passed.
'''
#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    #Remove pass and write the logic here
    sum=0
    if filter_func==None:
        for i in list_of_num:
            sum+=i
    elif filter_func==even:
        list=even(list_of_num)
        for i in list:
            sum+=i
    elif filter_func==odd:
        list=odd(list_of_num)
        for i in list:
            sum+=i
    return sum
    

def even(data):
    list=[]
    for i in data:
        if i%2==0:
            list.append(i)
    return list
    
def odd(data):
    list=[]
    for i in data:
        if i%2!=0:
            list.append(i)
    return list
    
sample_data = range(1,11)
print(sum_of_numbers(sample_data,None))
