'''
Problem Statement:
Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.
Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder. Consider the range to be from 1 to 10 (both inclusive).
Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.
Example:
Input Queue: 13983, 10080, 7113, 2520, 2500 (front - rear)
Output Queue: 10080, 2520 (front-rear)
Solution:
'''

'''
Created on Oct 20, 2019
@author: HITMAN
'''
#lex_auth_0127439036253470721632

class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

def check_numbers(number_queue):
    
    list1=[]
    list2=[]
    
    while not number_queue.is_empty():
        list1.append(number_queue.dequeue())
    
    for item in list1:
        flag=1
        for j in range(1,11):
            if item%j!=0:
                flag=0
                break
        if flag==1:
            list2.append(item)
    solution_queue1=Queue(len(list2))
    for item in list2:
        solution_queue1.enqueue(item)
    return solution_queue1

#Add different values to the queue and test your program
number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
check_numbers(number_queue)
