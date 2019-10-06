'''
Created on Oct 6, 2019

@author: HITMAN

Problem Statement: 
Write a python function, find_pairs_of_numbers() which accepts a list 
of positive integers with no repetitions and returns count of pairs of 
numbers in the list that adds up to n. The function should return 0, 
if no such pairs are found in the list.

Solution:
'''

#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    list=num_list
    count=0
    for i in list:
        for j in list:
            if i+j==n:
                count+=1
    return count//2

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))

