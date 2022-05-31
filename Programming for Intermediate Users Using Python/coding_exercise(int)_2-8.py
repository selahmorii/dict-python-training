# USING DICTIONARIES

# eliminating one pair through .pop()
shopping_list = {"chicken": 8, "apple": 6,"cucumbers": 3, "milk": 2, "oranges": 4}
acquired = shopping_list.pop("oranges")
print(shopping_list)
'''Output: 
{'chicken': 8, 'apple': 6, 'cucumbers': 3, 'milk': 2}'''

# using .keys()
speakers ={"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
print(speakers.keys()) #getting the names of speakers
'''OUTPUT:
dict_keys(['Sir Rafael', 'Ms. Joan', 'Ms. Dana'])
'''

# using .get()
swim_tryout = {"Carl": "passed", "Quentin": "failed", "John Y.": "passed", "Peter": "failed", "Max T.": "passed", "Joseph": "passed", "Jone": "failed", "Jorge": "failed", "George": "passed", "Ben": "passed", "Jerome": "passed", "Rick": "failed", "Max G.": "failed", "John P.": "failed", "Vince": "passed"}

friend = swim_tryout.get("Jorge")
print(friend)

'''OUTPUT: failed'''


# notes to self:
# can use it in a variable or within the print fxn. important thing is that the pop, get, key method are attached to the dictionary
# like: swim.pop("insert key here") 
# tho with .key() i think , it's not necessary to put something inside the () (not sure tho hehe)