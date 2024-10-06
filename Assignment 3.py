#Input Weight

height_input = input("Please enter your height in meters: ")
weight_input = input("Please enter your weight in kilograms: ")

#Convert Input
weight = float(weight_input)
height = float(height_input)

#Calculating BMI
BMI = weight/(height ** 2)

#Output
print("Your BMI is:", BMI)