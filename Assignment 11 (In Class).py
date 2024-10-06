#Initialize a flag for input validation
valid_input = False

#Loop until valid input is received
while not valid_input:
    user_input = input("Enter a positive number: ")

#Check if the input is a positive number,
    if user_input.isdigit():
        num = int(user_input) #Converting the string input into an integer, which will be stored in the num variable
        if num > 0:
            valid_input = True
        else:
            print("Please enter a positive number")
    else:
        print("That's not a valid number. Please try again! ")


#Generate the Collatz Sequence
print("Collatz Sequence")

while num != 1:
    print(num, end=" ")
    if num % 2 == 0:  #This is saying, if num is dividable by 2, then divide it by 2
        num //= 2
    else:
        num = 3 * num + 1
print (num)