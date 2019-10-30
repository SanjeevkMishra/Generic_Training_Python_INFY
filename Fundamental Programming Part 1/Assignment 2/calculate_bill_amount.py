'''
Problem Statement
FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.

A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that
they get more orders for their non-vegetarian combo than the vegetarian combo.
Solution:-
'''
#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if(food_type=="N" and quantity_ordered>0 and distance_in_kms>0):
        
            if(distance_in_kms>0 and distance_in_kms<=3):
                bill_amount = quantity_ordered*150
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount = quantity_ordered*150 + (distance_in_kms-3)*3
            elif(distance_in_kms>6):
                bill_amount = quantity_ordered*150 + (distance_in_kms-6)*6 +3*3
                 
    elif(food_type=="V" and quantity_ordered>0 and distance_in_kms>0):
        
            if(distance_in_kms>0 and distance_in_kms<=3):
                bill_amount = quantity_ordered*120
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount = quantity_ordered*120 + (distance_in_kms-3)*3
            elif(distance_in_kms>6):
                bill_amount = quantity_ordered*120 + (distance_in_kms-6)*6 +3*3
                 
    else:
        bill_amount=-1
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)

