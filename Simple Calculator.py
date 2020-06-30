# Simple Calculator

operation = input("Select Operation To Perform: Add\Subtract\Multiply\Divide ")   

if (operation == "Subtract" or operation == "Divide" or
    operation == "Add" or operation=="Multiply") :
    print("You selected:{}".format(operation))
    print("pls keep in mind that the order of the numbers matters")
    
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(num1)
print(num2)    

result = 0
try:
    num1,num2 = float(num1),float(num2)
    if operation == "Add":
        result = num1 + num2
        print("{} + {} = {}".format(num1,num2,result))
    elif operation == "Subtract":
        if max(num1,num2) ==num1:
            result = num1 - num2
        else:
            result = num2 - num1
        print("Result = ", result)
    elif operation == "Multiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1,num2,result))
    elif operation == "Divide":
        result = num1/num2
        print("{} / {} = {}".format(num1,num2,result))
    else:
        print("Sorry,but '{}' is not an option.".format(operation))
        
except:
       print("Error: improper number used.Please try again")



    
