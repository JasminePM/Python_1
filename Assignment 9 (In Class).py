
#Prompt the user to enter a single character
char_input = input("Please enter a single character: ")

#Checking to make sure they enter only one character and is a letter
if len(char_input) == 1 and char_input.isalpha():
    #Convert the character to a lowercase
    char = char_input.lower()

    if char  in "aeiou":
        print("The character is vowel.")
    else:
        print("The character is a consonant. ")
#if character length is not equal to 1 (single letter)
else:
    if len(char_input) != 1:
        print('Error: Please enter only one character. ')
    else:
        print('Error: The input is not a letter')


