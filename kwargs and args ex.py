def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg , end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
         print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
        
    




shipping_label("Dr","Spongebob","Squarepants",
            street="123 Fake St",
            apt="#100",
            city="Detorit",
            state="MI",
            zip="546")