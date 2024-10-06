#Input
hour_input = float(input("Please input time duration in hours:"))

#Convert hours to seconds
minutes = hour_input * 60
seconds = hour_input * 3600

#Output
print("This is your time converted to minutes and seconds", minutes, seconds)
