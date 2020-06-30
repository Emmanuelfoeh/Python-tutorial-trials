# Displaying your favorite food
import csv

def line():
    print("*"* 50 )
    
def FavoriteFood():
    with open("FavFood.csv",mode = "a",newline = "") as file:
        writer = csv.writer(file,delimiter = ",")
        favoriteFood = input("Enter your favorite food: ")
        rate = int(input("Rate your Favorite Food: "))
        writer.writerow([favoriteFood,rate])
def ShowFood():
    
    with open ("FavFood.csv",mode = "r") as file:
        reader = csv.reader(file)
        print("Favorite Food\t\tRating")
        for food in reader:
            print("{}".format(food))
            
active = True
while active:
    line()
    print("1.Enter your favorite food and rate it\n2.Show rating of food.\n3. quit ")
    choice = input("Enter your choice: ")
    line()
    if choice == "1":
        FavoriteFood()
    elif choice == "2":
        ShowFood()
    elif choice == "quit":
        active = False
    
    
