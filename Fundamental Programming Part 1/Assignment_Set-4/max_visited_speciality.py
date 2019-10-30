'''
Problem Statement:
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient 
along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a 
dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
} 

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
Solution:
'''
#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    
    p=o=e=0
    for i in range(1,len(patient_medical_speciality_list),2):
        if patient_medical_speciality_list[i]=='P':
            p+=1
        elif patient_medical_speciality_list[i]=='O':
            o+=1
        elif patient_medical_speciality_list[i]=='E':
            e+=1
    if p>o and p>e:
        max=p
    elif o>p and o>e:
        max=o
    else:
        max=e
    if max==p:
        speciality="Pediatrics"
    elif max==o:
        speciality="Orthopedics"
    else:
        speciality="ENT"
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
