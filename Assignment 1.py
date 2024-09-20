#Input for 3 different variables, this is the first ask


#We put float because the principal amount can be a decimal, and input will prompt to user to put an amount
principal = float(input("Enter the principal amount: "))
interest = float(input("Enter interest rate: "))
time = float(input("Enter the time period in years: "))

#Processing: Calculate the simple interest rate, this is the second ask

# * means multiple, and / is to divide, note we put all 3 variables in parenthesis so that the multiple together first before dividing
simple_interest = (principal * interest * time) / 100

#Output

#We use the comma, so we can have one type of data value and use another on the same line
print("Simple Interest is: ", simple_interest)