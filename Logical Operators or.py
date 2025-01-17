#Logical operator= execute multiple statements
#       Types: OR,AND,NOT
#       OR:one condition must be true
#       AND:Both statements be true
#       NOT:negation(converts true into false)

temp=25
is_raining=False

if temp>35 or temp<0 or is_raining:
    print("The outdoor event is cancelled")

else:
    print("The outdoor event is going to be held")