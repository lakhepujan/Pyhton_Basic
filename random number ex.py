#Python number guessing game

import random

lowest_num=1
highest_num=100
answers= random.randint(lowest_num,highest_num)
guesses=0
is_running=True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
   
    guess = input("Enter a digit")
   
    if guess.isdigit():
       guess=int(guess)
       guesses+=1
       

       if guess < lowest_num or guess > highest_num:
            print("Guess out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")     
       elif guess <answers:
            print("Too Low! Try again")
       elif guess>answers:
            print("Too High! Try again") 
       else:
            print(f"Correct! The answes is {answers}")
            print(f"Number of guesess : {guesses}")
            is_running=False

    else:
            print("Invalid Guess")  
            print(f"Please select a number between {lowest_num} and {highest_num}") 
