# Parent Class , Sub classes

class ClubMembers:
    def __init__(self, name, bday, age, food, goal):
        self.name = name
        self.bday = bday
        self.age = age
        self.food = food
        self.goal = goal
    
    def display1(self):
        print("Welcome New Member of the Club!")
        print("Infos about the member: ")
        print("Name: ", self.name)
        print("Birthday: ", self.bday)
        print("Age: ", self.age)
        print("Favorite food: ",self.food)
        print("Goal in life: ", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, bday, age, food, goal, position):
        super().__init__(name, bday, age, food, goal)
        self.position = position

    def display2(self):
        print("Our new club officer!")
        print("Infos about the new officer: ")
        print("Name: ", self.name)
        print("Position: ", self.position)
        print("Birthday: ", self.bday)
        print("Age: ", self.age)
        print("Favorite food: ",self.food)
        print("Goal in life: ", self.goal)

m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.display1()
print("\n") #line break for the output
o_4.display2()

'''
OUTPUT:
Welcome New Member of the Club!
Infos about the member: 
Name:  Tom
Birthday:  January 16
Age:  14
Favorite food:  Ice cream
Goal in life:  To be happy


Our new club officer!
Infos about the new officer:
Name:  Vera
Position:  Treasurer
Birthday:  June 22
Age:  16
Favorite food:  Beef stroganoff
Goal in life:  To be the world's greatest chef
'''
# slowed down on this topic as I'm getting confused hehe. hopefully i'll get the hang of it 