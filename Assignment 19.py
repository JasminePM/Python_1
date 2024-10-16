# Develop a function called  sort_list that takes a list of
# numbers as input and returns a new list
# containing the same elements sorted in ascending order.

def sort_list(list1):
    ascending_list = sorted(list1)
    return ascending_list

#Applying the Function
lista = [5,4,3,2,1]

results = sort_list(lista)
print(results)
