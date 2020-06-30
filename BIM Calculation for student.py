# BIM calculation for students

def BIM():
	w = int(input("Enter weight: "))
	H = int(input("Enter height: "))
	bmi = (w/H**2)
	print("The BIM is: {0.2f}".format(bmi))
	#return bmi
BIM()    
