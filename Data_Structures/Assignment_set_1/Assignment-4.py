'''
Problem Statement:
The Indian Cricket Board has decided to send its best players to ICC World Cup. They have chosen the best 11 players for the match.
The player’s names and their experiences in years are as given below.

 Name	 Dhoni	 Virat	 Rohit	 Raina	 Jadeja	 Ishant	 Shikhar	 Axar	 Ashwin	 Stuart	 Bhuvneshwar
 Experience	15	10	12	11	13	9	8	7.5	6	7	5
The players should be sent in for the batting based on their experience, i.e. the priority would be given to the player who has got the 
highest experience. At the last moment, the captain has decided that the player who has got the highest experience should bat at the 4th 
position.

Use the Player class and players_list provided to implement the class Game as given in the class diagram.

1. In the constructor of Game class, initialize players_list with list of players

2. Display the name and experience of the players after sorting the players based on their experience(descending order)

3. Display the name and experience of the players after moving the first player (0 index position) to the 4th (3 index position) position.

Solution:

'''
#DSA-Assgn-4

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

class Game:
    def __init__(self,players_list):
        self.__players_list=players_list
    
    def sort_players_based_on_experience(self):
        list2=[]
        for item in self.__players_list:
            list2.append(item.get_experience())
        list2.sort()
        list2.reverse()
        
        list1=[]
        for item1 in list2:
            for item2 in self.__players_list:
                if item1==item2.get_experience() and item2 not in list1:
                    list1.append(item2)
                    break
        self.__players_list=list1
    def shift_player_to_new_position(self,
                                     old_index_position,new_index_position):
        if old_index_position<new_index_position:
            temp=self.__players_list[old_index_position]
            self.__players_list.remove(self.__players_list[old_index_position])
            self.__players_list.insert(old_index_position,self.__players_list[new_index_position-1])
            self.__players_list.remove(self.__players_list[new_index_position])
            self.__players_list.insert(new_index_position,temp)
                    
        elif old_index_position>new_index_position:
            temp=self.__players_list[new_index_position]
            self.__players_list.remove(
                self.__players_list[new_index_position])
            self.__players_list.insert(
                new_index_position,
                self.__players_list[old_index_position-1]) 
            self.__players_list.remove(
                self.__players_list[old_index_position])
            self.__players_list.insert(old_index_position,temp)
            
    def display_player_details(self):
        for item in self.__players_list:
            print(item)
            
player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
#Create object of Game class, invoke the methods and test your program
G1=Game(players_list)
G1.display_player_details()
G1.shift_player_to_new_position(2, 5)
print("\n\n")
G1.display_player_details()
