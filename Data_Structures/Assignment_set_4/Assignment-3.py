'''

Problem Statement:
Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words. The task is to find the unknown
words (other than the words they already know) from the given text. Write a python function which accepts the text and the known list of 
words and returns the set of unknown words found.

Return -1 if there are no unknown words.

 
Sample Input:      Text: "the sun rises in the east"    ,
                   Vocabulary: ["sun","in","east","doctor","day"]
Expected Output:   {'rises', 'the'}

Solution:
'''
#lex_auth_0127667326864670723497

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    list1=text.split(" ")
    set1=set()
    flag=0
    for item in list1:
        if item not in vocabulary:
            set1.add(item)
            flag=1
    if flag==1:
        return set1
    else:
        return -1
        

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)




