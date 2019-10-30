'''
Problem Statement
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
Solution:
'''
#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    common=''
    flag=0
    for i in range(0,len(msg1)):
        for j in range(0,len(msg2)):
            if msg1[i]!=" ":
                if msg1[i]==msg2[j]:
                    if msg1[i] not in common:
                        common=common+msg1[i]
                        flag=1
    #my_common=set(common)
    if flag==1:                
        return common
    elif flag==0:
        return -1
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
