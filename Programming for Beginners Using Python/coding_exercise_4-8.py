#Loops and Iteration

# FOR LOOPS

f =["table", "chair", "cabinet", "desk", "couch"]

for x in f:
    if x == "cabinet":
        continue
    print(x)

'''
OUTPUT:
table
chair
desk
couch
'''

# WHILE Loops

i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15")

'''
OUTPUT:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
i is no longer less than 15
'''