#collection= a "variable" that contains multiple data

#list =[] are ordered  and changeable duplicates are ok
#sets ={} are unordered and immutable . can add or remove duplicates are not allowed
#tupele =() ordered and unchangeable duplicates ok faster

fruits = ["apple", "banana", "grapes", "orange"]

#print(dir(fruits)) provides function that can be used in list,set and tuple
#print(help(fruits))  provides details of the function
#print(len(fruits)) prints len of the collection variable

# fruits[0]= "pineapple"        adds pineapple to index 0
#fruits.append("pineapple")     adds pineapple to last place
#fruits.remove("apple")         removes the element
#fruits.insert(0,"pineapple")   insets the element at the given index
#fruits.sort()                     sorts the elements in ascending/alphabetical order
#fruits.reverse()       reverse the order of the list
# fruits.clear()        clears the list
#print(fruits.index("apple")) provides index of the corresponding elements
print(fruits.count("apple"))


#for fruit in fruits:
#    print(fruit)
#print(fruits)