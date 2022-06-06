#Handling, Creating and Writing a File

# write
f = open("newfile1.txt", "w")
f.write("It's easier and fun to learn.")
#append
f = open("newfile1.txt", "a")
f.write("\nI will study or review Statistics.")
f.write("\nI will apply this on improving my data analytics skills")
f.write("\nMy goals are to bgrow professionally and have a fulfilling career.")
f = open("newfile1.txt", "r")
print(f.read())
f.close()

'''
Initial Question:
What do I like about learning Python?
Appended my answers to these questions:
> What do I plan to do after learning Python?
> How do I apply what I've learned?
> What are my goals?
'''