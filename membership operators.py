grades = {"Sandy" : "A",
            "Squidward" :"B",
            "Patrik" : "C",
            "Spongebob" : "D"}

student = input("Enter the name of a student")

if student in grades:
    print(f"{student} grade is {grades[student]}")
else:
    print(f"{student} not found")