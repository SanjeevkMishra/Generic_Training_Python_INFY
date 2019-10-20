'''
Problem Statement:
Given a linked list of characters. Write a python function to return a new string that is created by appending all the characters given in 
the linked list as per the rules given below.

Rules:

1. Replace '*' or '/' by a single space

2. In case of two consecutive occurrences of '*' or '/' , replace those two occurrences by a single space and convert the next character 
to upper case.

Assume that 

1. There will not be more than two consecutive occurrences of '*' or '/'

2. The linked list will always end with an alphabet

Sample Input	Expected Output
 A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y	 An Apple a day Keeps A Doctor Away
 
 Solution:
 '''
 #lex_auth_0127438603766333441613

class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


def create_new_sentence(word_list):
    new_sentence=""
    temp=word_list.get_head()
    count=0
    '''
    while temp!=None:
        if temp.get_data() not in ['*','/']:
            new_sentence+=temp.get_data
        
        elif temp.get_data() in['*','/']:
            
        
    
    '''
    flag=0
    while(temp!=None):
        if temp.get_data() not in ['*','/'] and flag==0:
            new_sentence+=temp.get_data()
            temp=temp.get_next()
        elif temp.get_data() in ['*','/']:
            if temp.get_next().get_data() not in ['*','/']:
                new_sentence+=" "
                temp=temp.get_next()
            elif temp.get_next().get_data() in ['*','/']:
                new_sentence+=" "
                temp=(temp.get_next()).get_next()
                flag=1
        elif temp.get_data() not in ['*','/'] and flag==1:
            new_sentence+=(temp.get_data()).upper()
            flag=0
            temp=temp.get_next()

    return new_sentence

word_list=LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result=create_new_sentence(word_list)
print(result)



