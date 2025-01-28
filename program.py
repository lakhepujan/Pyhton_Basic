#concession stand program 

menu = {"momos":90,
         "chowmein":120,
         "burger" : 100,
         "sausage": 50,
         "aalu" : 40  }

cart=[]
total=0
 

print("---------- MENU -----------") 
for keys,values in menu.items():
    print(f"{keys:10}:{values}")

print("-----------------------------")

while True:
    food = input("Enter the food to order (q to quit):").lower()
    
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)



print("---------- YOUR ORDER----------")
for food in cart:
    total+=menu.get(food)
    print(food)
    
print("---------- TOTAL ---------------")
print(f"The total amount is : {total}")


