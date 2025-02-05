#Python Slot Machine
import random

def spin_row():
   symbols =['🍒' ,'🍉', '🔔', '🍋', '⭐']
   return [random.choice(symbols) for symbol in range (3)]
   

def print_row(row):
    print("*******************************")
    print(" | ".join(row))
    print("*******************************")

def payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0]== '🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*5
        elif row[0] == '🔔':
            return bet*1
        elif row[0] == '🍋':
            return bet*2
        elif row[0] == '⭐':
            return bet*5
    return 0



def main():
   balance = 100
   print("*******************************")
   print("Python Slot Machine")
   print("Symbols : 🍒 🍉 🔔 🍋 ⭐")
   print("*******************************")

   while balance >0:
       print(f"Current Balance $ {balance}")

       bet = input("Enter the bet amount")

       if not bet.isdigit():
           print("Please enter a valid number")
           continue
       
       bet = int(bet)

       if bet > balance:
           print("Insufficient Funds")
           continue
       elif bet <=0:
           print("Bet cannt be negative or zero")
           continue
       balance-=bet

       row = spin_row()
       print("Spinning.........\n")
       print_row(row)

       payouts =payout(row ,bet) 

       if payouts >0:
           print(f"You won $ {payouts}")
       else:
           print("You lost this round")
       balance+=payouts
       
   
if __name__ == '__main__':
    main()  