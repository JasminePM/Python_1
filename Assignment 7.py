time_input = int(input('Please input a year: '))

#Determining whether the year is a leap year or no

#Divisible by 400 and 100
if (time_input% 400 == 0) and (time_input % 100 == 0):
    print("This is a leap year")
    #Divisible by 4 and not visible by 100
elif (time_input % 4 == 0) and (time_input % 100 != 0):
    print ("This is a Leap Year")
else:
    print("This is not a leap year")