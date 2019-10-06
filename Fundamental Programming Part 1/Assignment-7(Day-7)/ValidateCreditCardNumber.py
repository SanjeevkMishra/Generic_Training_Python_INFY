'''
Created on Oct 6, 2019

@author: HITMAN

Problem Statement:

Use Luhn algorithm to validate a credit card number.
A credit card number has 16 digits, the last digit being the check 
digit. A credit card number can be validated using Luhn algorithm as 
follows:

Step 1a: From the second last digit (inclusive), double the value of 
every second digit.
Suppose the credit card number is 1456734512345698.
Take the double of 9,5,3,1,4,7,5 and 1
i.e., 18, 10, 6, 2, 8, 14, 10 and 2

Note: If any number is greater than 9, then sum the digits of that 
number.
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2

Step 1b: Sum the numbers obtained in Step 1a.
i.e., 34

Step 2: Sum the remaining digits in the credit card and add it 
with the sum from Step 1b.
i.e., 34 + (8+6+4+2+5+3+6+4) = 72

Step 3: If the total is divisible by 10 then the number is valid else 
it is not valid.
Write a function, validate_credit_card_number(), which accepts a 
16 digit credit card number and returns true if it is valid as per 
Luhn’s algorithm or false, if it is invalid.

Solution:
'''
#lex_auth_01269445968039936095
def sum_digit(number):
    num=number
    sum=0
    while(num!=0):
        rem=num%10
        sum+=rem
        num//=10
    return sum
def validate_credit_card_number(card_number):
    #start writing your code here
    string=str(card_number)
    list=[]
    for i in string:
        list.append(int(i))
    sum=0
    for i in range(len(string)-2,-1,-2):
        list[i]*=2
        if list[i]>9:
            list[i]=sum_digit(list[i])
    for i in range(0,len(string)):
        sum+=list[i]
    if sum%10==0:
        return True
    else:
        return False
    
card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
 
