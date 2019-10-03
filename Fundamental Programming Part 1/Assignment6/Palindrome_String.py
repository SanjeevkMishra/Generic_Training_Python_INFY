Problem Statement: Write a recursive function, is_palindrome() to find out 
whether a string is a palindrome or not. The function should return true, if it is a 
palindrome. Else it should return false. 

Solution:

#lex_auth_01269442114344550475

def is_palindrome(word):
	string=word.lower()
	list1=[]
	list2=[]
	for i in string:
		list1+=i

	for i in list1[::-1]:
		list2+=i
	if list1==list2:
		return True
	else:
		return False

result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
