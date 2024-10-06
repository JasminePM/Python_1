#Input
currency_USD = float(input("Please input currency in USD: "))

#Processing, convert to EUR
#The formula is (currency of interest * exchange rate)
currency_EUR = currency_USD * 0.91

#Output
print("This is your USD currency converted to EUR: ", currency_EUR)