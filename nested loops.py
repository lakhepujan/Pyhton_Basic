#nested loop: a loop within a loop
#              outer loop:
#                   inner loop:      

rows = int(input("Enter the number of rows"))
#columns = int(input("Enter the number of columns"))
#symbol = input("Enter a symbol to use")

for x in range(rows):
    for y in range(rows-x-1): #for space
        print(" ",end="")
    for y in range(x+1):    #prints +1 star
         print("*",end=" ")
    print()

