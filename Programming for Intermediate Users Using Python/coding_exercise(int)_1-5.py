# Remember Coffee Palace in Beginners Course, now this gonna be Coffe Palace 2.0

class Customers:
    greeting = "Welcome to Coffee Palace!"
    def __init__(self,name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe late", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

# ding!
print(Customers.greeting)
# 2 customers just came in.. here goes their orders and infos!
print("For customer 1: ", c_2.name,", ", c_2.beverage,", ", c_2.food,". For a total of ", "$", c_2.total,".")
print("For customer 2: ", c_4.name,", ", c_4.beverage,", ", c_4.food,". For a total of ", "$",  c_4.total,".")
print("Enjoy your food and stay here!")


# just added some storytelling in the code. hehe ^-^'

'''
OUTPUT:
Welcome to Coffee Palace!
For customer 1:  Elaine ,  Strawberry frappuccino ,  Tuna wrap . For a total of  $ 270
For customer 2:  Jerry ,  Caramel macchiato ,  Glazed doughnut . For a total of  $ 230
Enjoy your food and stay here!
'''