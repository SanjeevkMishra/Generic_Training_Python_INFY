'''
Created on Oct 5, 2019

@author: HITMAN

Problem Statement:

Write a python program to help an airport manager to generate few 
statistics based on the ticket details available for a day.Go through 
the below program and complete it based on the comments mentioned in it.

Note: Perform case sensitive string comparisons wherever necessary.

Solution:

#lex_auth_0127382193364008961449

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number
'''
#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    list=[]
    count=0
    for i in ticket_list:
        list=i.split(":")
        if list[2]==destination:
            count+=1
    return count

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for i in ticket_list:
        list1=i.split(":")
        list2.append(list1[0])
    
    for i in  list2:
        num=0
        string=''
        if i[:2] not in list3:
            num=list2.count(i)
            list3.append(i[:2])
            string+=i
            string+=":"
            string+=str(num)
            list4.append(string)
    return list4    
    

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    list=find_passengers_per_flight()
    list3=[]
    list4=[]
    dict={}
    for i in list:
        list3=i.split(":")
        list4.append(int(list3[1]))
        dict[list3[0]]=int(list3[1])
    list4.sort()
    list4.reverse()
    list=[]
    for i in list4:
        for key,value in dict.items():
            string=''
            if i == dict[key]:
                string+=key
                string+=":"
                string+=str(dict[key])
                list.append(string)
    return list 

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
