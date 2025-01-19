principle=0
time=0
rate=0


while principle<=0:
    principle=float(input("Enter the principle"))
    if principle<=0:
     print("Principle cant be less than or equal to zero")



while time<=0:
    time=int(input("Enter the time amount"))
    if time<=0:   
      print("Time cant be less than or equal to zero")
   



while rate<=0:
    rate=float(input("Enter the rate amount"))
    if rate<=0:
        print("rate cant be less than or equal to zero")
   


total= principle *pow((1+rate/100),time)

print(f"The total balance after {time} year/s : {total:.2f}")
