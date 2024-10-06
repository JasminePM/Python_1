#Input
x1 = float(input("Please input point for x1: "))
y1 = float(input("Please input point for y1: "))
x2 = float(input("Please input point for x2: "))
y2 = float(input("Please input point for y2: "))
#Processing: Calculating the distance between the two points
x_squared = (x2 - x1) ** 2
y_squared = (y2 - y1) ** 2 #squared
distance_squared = x_squared + y_squared

distance = distance_squared ** 0.5 #Squareroot

#Output
print("The distance between these point is: ", distance)
