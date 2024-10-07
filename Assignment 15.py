
#The Efficient Way
def power(base, exponent):

    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base,-exponent) #Changes the exponent to positive
    else:
        return base * power(base, exponent - 1)

print(power(2,3))
print(power(5,0))
print(power(2, -3))
