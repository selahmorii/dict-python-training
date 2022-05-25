# Coffee Palace

class Customers:
    greetings = "Welcome to the Coffee Palace!"

c_1=Customers()

c_1.name = "Samirah"
c_1.beverage = "Iced caffe latte"
c_1.food = "Cinnamon roll"
c_1.total = 225

c_2=Customers()

c_2.name = "Jerry"
c_2.beverage = "Caramel macchiato"
c_2.food = "Glazed doughnut"
c_2.total = 230

print(Customers.greetings)
print(c_1.beverage)
print(c_2.food)

'''
OUTPUT:
Welcome to the Coffee Palace!
Iced caffe latte
Glazed doughnut
'''