temp=20
is_sunny=False

if temp>=28 and  not is_sunny:
    print("It is hot outside")
    print("It is Cloudy")

elif temp<=0 and  not is_sunny:
    print("It is cold outside")
    print("It is Cloudy")
    
elif temp>=28 and not is_sunny:
    print("It is hot Outside")
    print("It is cloudy")

elif temp<28 and temp>0 and  not is_sunny:
    print("It is warm Outside")
    print("It is Cloudy")    