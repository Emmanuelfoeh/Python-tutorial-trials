# Add write up to emma.txt file
'''
path = "C:/Users/BLESS/Desktop/python_self/emma.txt"

WriteEmma = open(path, "a")
WriteEmma.writelines("Hello Emmanuel\nHow are you doing?\njust want to know how far with the project")
WriteEmma.close()

ReadEmma = open(path, "r")
#print(ReadEmma.readlines())
for line in ReadEmma.readlines():
    print(line),
ReadEmma.close()

#path2 = "C:/Users/BLESS/Desktop/python_self/poem.txt"
Readpoem =open("poem.txt", "r")
for line in Readpoem.readlines():
    print(line),
Readpoem.close()    
'''
import os
path_3 = "C:/Users/BLESS/Desktop/toDoList.txt"
myFile = os.path.join(path_3)

with open(myFile, "r") as ReadtoDoList:
    for lines in ReadtoDoList.readlines():
         print(lines)
   
