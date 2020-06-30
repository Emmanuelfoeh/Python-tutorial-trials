# Creating a Company Recipt

P1_name,P1_price = "Table",20
P2_name,P2_price = "Chair",15
P3_name,P3_price = "Table cloth",10

# Company Info
Company_name = "Emmanuel Furniture LMD"
Company_address = "123 Emma St."
Company_City = "Ho"
Appreciation = "Thanks for shopping with us"

#Creating top border
print("~" * 80)

#Displaying the Company Info
print("\t\t{}".format(Company_name.upper()))
print("\t\t{}".format(Company_address.upper()))
print("\t\t{}".format(Company_City.upper()))

print("~"*80)

print("\t\tProduct Name\t\tProduct Price")

# Printing each product

print("\t\t{}\t\t\t{} Cedis".format(P1_name,P1_price))
print("\t\t{}\t\t\t{} Cedis".format(P2_name,P2_price))
print("\t\t{}\t\t{} Cedis".format(P3_name,P3_price))

print("*"*80)

Total = P1_price + P2_price + P3_price

print("\t\tTotal\t\t\tCedis{}".format(Total))
print("+"*80)
print("\t\t",Appreciation)
print("+"*80)


