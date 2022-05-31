# Dictionary

flavor = ["vanilla" , "chocolate" , "strawberry" , "cookies n cream" , "bubblegum"]
toppings = ["almonds" , "banana slices" , "chocolate syrup" , "caramel syrup" , "white chocolate chips"]

ice_cream = dict(zip(flavor, toppings)) #using dict() and zip() fxn
print(ice_cream)
'''OUTPUT:
{'vanilla': 'almonds', 'chocolate': 'banana slices', 'strawberry': 'chocolate syrup', 'cookies n cream': 'caramel syrup', 'bubblegum': 'white chocolate chips'} 
'''

ice_cream["chocolate"] = "blueberries" #changing banna slices to blueberries
print(ice_cream)
''' OUTPUT: 
{'vanilla': 'almonds', 'chocolate': 'blueberries', 'strawberry': 'chocolate syrup', 'cookies n cream': 'caramel syrup', 'bubblegum': 'white chocolate chips'}  
'''

ice_cream.update({"matcha":"pistachios", "ube":"mango slices"}) #using .update() when adding new infos
print(ice_cream)
'''
OUTPUT:
{'vanilla': 'almonds', 'chocolate': 'blueberries', 'strawberry': 'chocolate syrup', 'cookies n cream': 'caramel syrup', 'bubblegum': 'white chocolate chips', 'matcha': 'pistachios', 'ube': 'mango slices'}
'''