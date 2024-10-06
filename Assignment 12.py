
#How to obtain the rows input from user
num = int(input("Please enter any number for rows of the right triangle : "))

#How to create rows that add 1 for each row
for i in range(0, num):
    for j in range(0, i+1):
        print("*", end="")
    print()

