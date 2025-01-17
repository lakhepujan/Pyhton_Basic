#Python Calculator Program

operator=input("Enter operator(+,-,/,*)")
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))

if operator=="+":
    print("Addition Operator")
    result=num1+num2
    print(result)
elif operator=="-":
    print("Subtraction Operator")
    result=num1-num2
    print(result)
elif operator=="*":
    print("Multiplication Operator")
    result=num1*num2
    print(result)
elif operator=="/":
    print("Division Operator")
    result=num1/num2
    print(result)
else:
    print(f"{operator} is not a valid operator")  