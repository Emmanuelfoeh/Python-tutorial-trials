# Comparing Age values
# Trying hand on user input

Age = input("pls enter your Age: ")

if (0 <= int(Age) <=12):
    print("Kid")
elif (13<= int(Age) <= 19):
    print("Teenger")
elif (20<= int(Age)<=30):
    print("Young Adult")
elif (31<= int(Age)<=64):
    print("Adult")
else:
    print("Senior Citizen")

