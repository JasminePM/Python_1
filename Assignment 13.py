string = str(input("Please enter any set of characters: "))
#How to reverse an input
reversed = (string[::-1])

if reversed == string:
    print("This is a Palindrome")
else:
    print("This is NOT a Palindrome")
