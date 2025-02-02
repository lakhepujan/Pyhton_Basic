def address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


address(street="123 Fake St",
        apt="100",
        city="Detorit",
        state="MI",
        zip="546")