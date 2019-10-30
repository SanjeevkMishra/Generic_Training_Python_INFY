'''
Problem Statement:
Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details 
mentioned below:
The ticket number should be generated as airline:src:dest:number
where
1.Consider AI as the value for airline
2.src and dest should be the first three characters of the source and destination cities.
3.number should be auto-generated starting from 101.

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket numbers.
Solution:-
'''
#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    string=" "
    if(no_of_passengers<5):
        for i in range(1,no_of_passengers+1):
            string= airline+':'+source[0:3]+':'+destination[0:3]+':'+str(100+i)
            ticket_number_list.append(string)
            
    elif(no_of_passengers>=5):
        for i in range(-5,0):
            string=airline+':'+source[0:3]+':'+destination[0:3]+':'+str(no_of_passengers+100+i+1)
            ticket_number_list.append(string)
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
Ticket_list=generate_ticket("AI","Bangalore","London",7)

for i in Ticket_list:
    print(i)
