#Prompting User to Enter their Age

age_input = input("Please enter your age: ")

#Check if the input is a number and not an empty string
if age_input.isdigit():
    age = int(age_input)
    #Ensure the age is positive
    if age > 0:
        #Classify the age into categories
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print ("Adult")
        else:
            print('Senior Citizen')
    else:
        print("Error: Age must be a positive integer.")
else:
    print("Error: Invalid input. Please enter a positive integer")
