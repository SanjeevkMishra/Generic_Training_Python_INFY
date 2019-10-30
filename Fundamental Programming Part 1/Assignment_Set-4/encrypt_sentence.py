'''
Problem Statement:
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted
message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Solution:
'''
#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    list1=sentence.split(' ')
    string=''
    sentence=''
    for i in range(0,len(list1)):
        if i%2==0:
            string1=list1[i][::-1]
            string+=string1  
            #string+=" "
        elif i%2!=0:
            string2=list1[i]
            string3=''
            string4=''
            for j in range(0,len(string2)):
                if string2[j]=='a' or string2[j]=='e' or string2[j]=='i' or string2[j]=='o' or string2[j]=='u':
                    string3+=string2[j]
                else:
                    string4+=string2[j]
            string+=string4+string3
        string+=" "
        sentence=string[:len(string)-1]
    return sentence
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
