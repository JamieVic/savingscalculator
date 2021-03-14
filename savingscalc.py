try:
    amount = float(input("Amount ($): "))
    interest = float(input("Interest Rate (%): "))
    years = int(input("Years: "))
except:
    print("Invalid character entered.")

rawResult = amount * ((1 + (interest / 100)) ** years)
result = "{:.2f}".format(rawResult)
print("After " + str(years) + " years, your balance will be at " + str(result) + ".")