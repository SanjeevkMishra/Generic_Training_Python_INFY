'''
Created on Oct 6, 2019

@author: HITMAN

Problem Statement
A teacher is in the process of generating few reports based on the 
marks scored by the students of her class in a project based assessment.
Assume that the marks of her 10 students are available in a tuple. 
The marks are out of 25.

Write a python program to implement the following functions:

1. find_more_than_average(): Find and return the percentage of students
who have scored more than the average mark of the class.

2. generate_frequency(): Find how many students have scored the same 
marks.
3. sort_marks(): Sort the marks in the increasing order from 0 to 25. 
The sorted values should be populated in a list and returned.

Solution:
'''
#lex_auth_01269438947391897654
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    #Remove pass and write your logic here
    sum=0
    for i in list_of_marks:
        sum+=i
    avg=sum/10
    count=0
    for i in list_of_marks:
        if i>avg:
            count+=1
    return (count*100)/10

def sort_marks():
    #Remove pass and write your logic here
    list=[]
    for i in list_of_marks:
        list.append(i)
    list.sort()
    return list

def generate_frequency():
    #Remove pass and write your logic here
    list=[0]*26
    for i in list_of_marks:
        list[i]+=1
    return list

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
