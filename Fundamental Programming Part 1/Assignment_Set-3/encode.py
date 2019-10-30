'''
Problem Statement
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be
replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
Solutions:-
'''
#lex_auth_012693816331657216161

def encode(message):
   
    start=0
    end=len(message)
    string=""
    i=0
    p=0
    while(i<end and p<end):
        p+=1
        num=message[i]
        count=0
        for j in range(i,end):
            if(num==message[j]):
                count+=1
                #i+=1
                if (j==end-1):
                    string+=str(count)
                    string+=num
                    i+=1
                    break
            else:
                string+=str(count)
                string+=num
                i=j
                break
        
    return string

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
