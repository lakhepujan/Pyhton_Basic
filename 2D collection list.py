
groceries=[["apple", "banana" ,"coconut" , "orange"],["potato", "carrots", "peas"], ["chicken", "mutton" ,"fish"]]


#print(groceries) prints every element in the 2D collection
#print(groceries[0][0]) prints element referenced by the indices

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()
