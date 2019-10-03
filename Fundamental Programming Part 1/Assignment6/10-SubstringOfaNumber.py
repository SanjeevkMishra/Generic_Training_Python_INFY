Problem Statement:

A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string 
and returns the list of 10-substrings of that string.

Solution:

#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    list=[]
    for i in num_str:
    	list.append(int(i))
    list1=[]
    for i in range(0,len(list)):
    	j=i
    	sum=0
    	string1=''
    	string3=''
    	while(True):
    		if j<len(list) and sum<10:
    			sum+=list[j]
    			string1+=str(list[j])
    			j+=1
    		else:
    			break
    	if sum==10:
    		list1.append(string1)
    		string3+=string1
    	while j<len(list) and list[j]==0:
    		string3+=str(list[j])
    		list1.append(string3)
    		j+=1
    return list1
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
