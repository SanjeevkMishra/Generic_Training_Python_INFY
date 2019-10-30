'''
Problem Statement
The Metro Bank provides various types of loans such as car loans, business loans and house loans to its account holders. Write a python 
program to implement the following requirements:

Initialize the following variables with appropriate input values:account_number, account_balance, salary, loan_type, loan_amount_expected 
and customer_emi_expected.

The account number should be of 4 digits and its first digit should be 1.

The customer should have a minimum balance of Rupees 1 Lakh in the account.

If the above rules are valid, determine the eligible loan amount and the EMI that the bank can provide to its customers based on their 
salary and the loan type they expect to avail.

The bank would provide the loan, only if the loan amount and the number of EMI’s requested by the customer is less than or equal to the 
loan amount and the number of EMI’s decided by the bank respectively.

Display appropriate error messages for all invalid data. If all the business rules are satisfied ,then display account number, eligible 
and requested loan amount and EMI’s.Test your code by providing different values for the input variables.

Solution:-
'''

#lex_auth_012693788748742656146

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    
    if(loan_type=="Car" or loan_type=="House" or loan_type=="Business"):
        num=str(account_number)
        if(len(num)!=4 or num[0]!='1'):
            print("Invalid account number")
            return
        elif(account_balance < 100000):
            print("Insufficient account balance")
            return
        
        if(loan_type=="Car" and customer_emi_expected<=36 and salary>25000 and loan_amount_expected <=500000):
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", 500000)
            print("Eligible EMIs :", 36)
            print("Requested loan amount:",loan_amount_expected )
            print("Requested EMI's:",customer_emi_expected)
            return
        elif(loan_type=="Car" and customer_emi_expected<=36 and salary<=25000 and loan_amount_expected <=500000):
            print("Invalid loan type or salary")
       # elif(loan_type=="Car" and customer_emi_expected>36 and salary>25000 and loan_amount_expected >500000 or loan_type=="Car" and loan_amount_expected>500000 and customer_emi_expected<=36 and salary<25000 ):
        #    print("Invalid loan type or salary")
         #   return
        
            
        elif(loan_type=="House" and customer_emi_expected<=60 and salary>50000 and loan_amount_expected <=6000000):
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", 6000000)
            print("Eligible EMIs :", 60)
            print("Requested loan amount:",loan_amount_expected )
            print("Requested EMI's:",customer_emi_expected)
            return
        elif(loan_type=="House" and customer_emi_expected<=60 and salary<=50000 and loan_amount_expected <=6000000):
            print("Invalid loan type or salary")
        
       # elif(loan_type=="House" and customer_emi_expected>60 and salary>50000 and loan_amount_expected >=6000000 or loan_type=="House" and customer_emi_expected<=60 and salary<50000 and loan_amount_expected >6000000):
        #    print("Invalid loan type or salary")
         #   return
        
        elif(loan_type=="Business" and customer_emi_expected<=84 and salary>75000 and loan_amount_expected<=7500000):
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", 7500000)
            print("Eligible EMIs :", 84)
            print("Requested loan amount:",loan_amount_expected )
            print("Requested EMI's:",customer_emi_expected)
            return
        elif(loan_type=="Business" and customer_emi_expected<=84 and salary<=75000 and loan_amount_expected<=7500000):
             print("Invalid loan type or salary")
        #elif(loan_type=="Business" and customer_emi_expected>84 and salary>75000 and loan_amount_expected>7500000 or loan_type=="Business" and customer_emi_expected<=84 and salary<75000 and loan_amount_expected>7500000):
         #   print("The customer is not eligible for the loan")
          #  return
        else:
            print("The customer is not eligible for the loan")
        
    else:
        print("Invalid loan type or salary")
        return
        
    
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)
