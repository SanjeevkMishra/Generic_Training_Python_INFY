Problem Statement:
Write a python function find_smallest_number() which accepts a number
n and returns the smallest number having n divisors. Handle the possible 
errors in the code written inside the function.

Solution:

#lex_auth_01269442760027340879

def find_smallest_number(num):
    n=1
    while(True):
    	no_of_factors=num_Factors(n)
    	if no_of_factors==num:
    		return n
    	else:
    		n+=1
def num_factors(n):
	factors=0
	for i in range(1,n+1):
		if n%i==0:
			factors+=1
	return factors

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
