'''
Problem Statement:
Given two lists, both having integer elements, write a python program using python lists to create and return a new list as per the rule given below:

If the double of an element in list1 is present in list2, then add it to the new list. 
 

Sample Input	Expected Output
 list1 - [11, 8,23,7,25, 15]
 list2 – [6, 33, 50,31, 46, 78, 16,34]	 new_list – [8,23,25]
 
 Solutions:
 
 '''
 
 #lex_auth_0127426336682147841449

def check_double(list1,list2):
    new_list=[]
    
    for item1 in list1:
        for item2 in list2:
            if item2==2*item1 and item1 not in new_list:
                new_list.append(item1)
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))
