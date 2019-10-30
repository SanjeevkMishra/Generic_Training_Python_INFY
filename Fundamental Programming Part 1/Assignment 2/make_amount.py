'''
Problem Statement
You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide
exact change. You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not
possible then display -1.
Solution:-
'''
#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    
    
    five=rupees_to_make//5
    if(five<=no_of_five):
        five_needed=five
        rupees_to_make-=five_needed*5
    elif(five>=no_of_five):
        five_needed=no_of_five
        rupees_to_make-=five_needed*5
    
    one=rupees_to_make//1
    
    if(one<=no_of_one):
        one_needed=one
    elif(one>=no_of_one):
        print(-1)
        return
    
    print("No. of Five needed :",five_needed)
    print("No. of One needed  :",one_needed)
        
    


    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
