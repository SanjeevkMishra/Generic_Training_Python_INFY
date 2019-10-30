'''
Problem Statement:
Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display 
the list.
Solution:
'''
#lex_auth_012693797166096384149

def find_leap_years(given_year):
    i=given_year
    list_of_leap_years=[]
    p=0
    while(i>=given_year and p<15):
        if(i%400==0 or (i%100!=0 and i%4==0)):
            list_of_leap_years.append(i)
            p+=1
        i+=1
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
 
