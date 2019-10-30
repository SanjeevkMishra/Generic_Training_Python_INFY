'''
Problem Statement:
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns
the abbreviated sentence. 

Rules are as follows: 
a. Spaces are to be retained as is 
b. Each word should be encoded separately

If a word has only vowels then retain the word as is

If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
Solution:
'''
#lex_auth_01269444961482342489

def sms_encoding(data):
    list=data.split(" ")
    string=''
    sentence=''
    for data in list:
        cons=0
        con_string=''
        for i in range(0,len(data)):
            if data[i] not in ['a','e','i','o','u','A','E','I','O','U']:
                cons+=1
                con_string+=data[i]
        if cons>=1:
            string+=con_string
        elif cons==0:
            string+=data
        string+=" "
        sentence=string[:len(string)-1]
    return sentence
data="I love Python"
print(sms_encoding(data))
