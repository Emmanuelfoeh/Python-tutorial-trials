def invest(amount, rate, time):
    
    print(amount)
    print(rate)
    for year in range(1,time+1):
        amount = amount*(1 + rate)
        print ("year {}: ${}".format(year, amount))

    print(invest(120,0.4,9))
    exit = input("enter")
