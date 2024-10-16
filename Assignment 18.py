#Create a function called  concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples

def concat_tuples(tuple1, tuple2):
    #Check to see that the inputs are tuples and if they are not, you give a ValueError exception
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise ValueError("Both inputs must be tuples.")

    results = tuple1 + tuple2
    return results

#Applying our function
try:
    tuplea = (1, 2, 3, 4)
    tupleb = (5, 6, 7, 8)

    results = concat_tuples(tuplea, tupleb)
    print(results)
except ValueError as e:  #If there is an error, then give me a ValueError exception (e is just a chosen variable to signify the valueerror)
    print(e)