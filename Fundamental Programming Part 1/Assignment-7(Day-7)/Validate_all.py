'''
Created on Oct 6, 2019

@author: HITMAN

Problem Statement:
Write a python program to validate the details provided by a user as 
part of registering to a web application.

Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets

Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number

Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com

All the functions should return true if the corresponding value is 
valid. Otherwise, it should return false.

Write a function validate_all(name,phone_no,email_id) which should 
invoke appropriate functions to validate the arguments passed to it 
and display appropriate message. Refer the comments provided in the 
code.

Solution:

'''
#lex_auth_012694465248329728100

def validate_name(name):
    #Start writing your code here
    if name==" " or len(name)>15:
        return False
    for i in name:
        if i.isdigit():
            return False
    return True
            

def validate_phone_no(phno):
    #Start writing your code here
    string=str(phno)
    if len(string)!=10:
        return False
    for i in string:
        if i.isalpha():
            return False
    list=[]
    for i in string:
        list.append(int(i))
    for i in range(1,len(string)):
        if list[i]!=list[i-1]:
            return True
    return False

def validate_email_id(email_id):
    #Start writing your code here
    if email_id.count("@")!=1 or email_id.count(".com")!=1:
        return False
    if email_id.endswith(".com")==False:
        return False
    if "gmail" in email_id or "yahoo" in email_id or "hotmail" in email_id:
        pass
    else:
        return False
    return True
    
def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")
    if validate_email_id(email_id)==False:
        print("Invalid email id")
    elif validate_name(name)==False:
        print("Invalid Name")
    elif validate_phone_no(phone_no)==False:
        print("Invalid phone number")
    else:
        print("All the details are valid")
#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
