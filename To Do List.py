#cREATING TO-DO-LIST
#Supper 30 movie to watch
#Freedom writers to watch

#Declear a list to score your do list
Dolist = []
#Function to add do-list
def AddList(lists):
    Dolist.append(lists)
    print("{} has been added".format(lists))

# To remove list item
def RemovedList(lists):
    try:
        if lists == Dolist.index(lists):
            Dolist.remove(lists)
        print("{} has been removed from the lists.".format(lists))
    except:
        print("Sorry,no such Dolist found.")

# Show list
def ShowList():
    #if Dolist:
     #   print("Lists of your ToDoList")
    for lists in Dolist:
        print("{} {}".format(Dolist.index(lists),lists))
    #else:
     #   print("Your list is empty")
        
# Function to clear the list
def ClearList():
    Dolist.clear()
    print("Your list is clear")

# The main function
def ToDoList():
    done = False
    while not done:
        print("Pls Enter any of the below")
        request = input("quit/add/remove/show/clear: ").lower()

        if request == "quit":
            print("Your daily tasks is set ")
            ShowList()
            done = True
            
        elif request == "add":
            lists = input("Add a task to your ToDoList: ").title()
            AddList(lists)
        elif request == "remove" :
            lists = input("Which list will you like to removed? ")
            RemovedList(lists)
        elif request == "show":
            ShowList()

        elif request == "clear":
            ClearList()

        else:
            print("Sorry,Not a function of this program")
ToDoList()        
