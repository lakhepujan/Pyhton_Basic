capitals={"USA":"Washington D.C",
          "India":"New Delhi",
          "China":"Bejing",
          "Russia":"Moscow"}

#print(dir(capitals)) shows attributes that can be used in dictationeries
# print(help(capitals)) in depth explanations of the attributes


#print(capitals.get("USA"))  gets vlaue associated with the key,
#           can be used with if statement 
#           get attribute checks if the key is in our dictaionary or not
#if capitals.get("Japan"):
#   print("This capital exists")
#else:
#    print("This capital doesnt exists")


#capitals.update({"Germany":"Berlin"})  used to add a additional key attribute or to change the existing key value
#capitals.pop("USA")        used to delete an element
#capitals.popitem()         used to delete latest key value
#capitals.clear()           deletes all key  value in the dictaionary
#keys=capitals.keys()       prints all the key in the dictationary without printing the values

#for keys in capitals.keys():
#    print(keys)

#values=capitals.values()       prints all the values in the dictationary can be used in for loop

#for keys,values in capitals.items():  items return dictationary object that returns value as 2D tuples
#    print(f"{keys}:{values}")