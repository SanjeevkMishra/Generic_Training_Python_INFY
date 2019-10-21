'''

Problem Statement:
The International Cricket Council (ICC) wanted to do some analysis of international cricket matches held in last 10 years.

Given a list containing match details as shown below:
[match_detail1,match_detail2……]

Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won

Example: AUS:CHAM:5:2 means Australia has participated in Champions Trophy 5 times and have won 2 times.

Write a python program which performs the following:

find_matches (country_name): Accepts the country_name and returns the list of details of matches played by that country.

max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which have won the maximum 
number of matches in that championship as the value.

find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number of matches in all 
championships. If both have won equal number of matches, return "Tie".

Perform case sensitive string comparison wherever necessary.
match_list – ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0',
'SA:CHAM:5:1', 'IND:WOR:2:1']

Solution:
'''
#lex_auth_0127667391112806403379

def find_matches(country_name):
    #Remove pass and write your logic here
    list=[]
    for data in match_list:
        if data[0:3]==country_name: 
            list.append(data) 
    return list
def max_wins():
    #Remove pass and write your logic here
    dict={}
    list1=[]
    for item in match_list:
        list2=item.split(":")
        if list2[1] not in list1:
            list1.append(list2[1])
    
    list=[]
    for data in list1: 
        max=-2
        for item in match_list:
            l1=item.split(":")
            if l1[1]==data and int(l1[3])>=max:
                max=int(l1[3])
        list.append(max)
         
    i=0
    for data in list1:
        list3=[]
        for item in match_list:
            l1=item.split(":")
            if l1[1]==data and int(l1[3])==list[i]:
                list3.append(l1[0])
        i+=1
        dict[data]=list3        
    return dict
def find_winner(country1,country2):
    #Remove pass and write your logic here
    list2=[]
    max1,max2=0,0
    for item in match_list:
        list1=item.split(":")
        if list1[0]==country1:
            max1+=int(list1[3])
            
        elif list1[0]==country2:
            max2+=int(list1[3])
    if max1>max2:
        return country1
    elif max1<max2:
        return country2
    else:
        return "Tie"

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()
print(max_wins())
