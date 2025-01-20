import time

my_time=int(input("Enter the time"))

for x in range(my_time, 0,-1): #can use reversed function too
    seconds = x % 60
    minutes = int(x / 60) %60
    hours = int(x / 3600)
    print(f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(3)


print("Times Up!!!")