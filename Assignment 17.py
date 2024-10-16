
#Develop a function called  find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.

#Function
def find_common_element(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements
    #set will intersect both lists, and create a new list with those
    #common elements and store it in the common_elements variable

#Applying the Function to see if it works
lista = [1,2,3,4,5]
listb = [1,3,6,8,9]

results = find_common_element(lista, listb)
print(results)