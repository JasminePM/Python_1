
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

#Applying the Function
num = int(input("Please input a number: "))

results = is_prime(num)
print(results)
