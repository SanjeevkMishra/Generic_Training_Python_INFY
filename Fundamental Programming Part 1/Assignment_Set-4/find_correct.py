'''
Problem Statement:
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.
Solution:-
'''
#lex_auth_01269444890062848087

def find_correct(word_dict):
    list=[0,0,0]
    for key,value in word_dict.items():
        match=0
        no_match=0
        
        if len(key)!=len(value):
            list[2]+=1
            continue
        for i in range(0,len(key)):
            if key[i]==value[i]:
                match+=1
            elif key[i]!=value[i]:
                no_match+=1
        if match==len(key):
            list[0]+=1
            continue
        elif no_match>0 and no_match<=2:
            list[1]+=1
            continue
        elif no_match>2:
            list[2]+=1
            continue
        
        
    return list
                
                

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
