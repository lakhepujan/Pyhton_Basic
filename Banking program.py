#Python Banking Program

def show_balance(balance):
    print("*****************************")
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount to be deposited $ "))
    
    if amount < 0:
        print("*****************************")
        print("Not a valid amount")
        return 0
    else:
        return amount
def withdrawl(balance):
    amount = float(input("Enter amount to be withdrawn $ "))
    if amount > balance:
        print("*****************************")
        print("Insufficient funds in account")
        return 0
    elif amount <= 0:
        print("*****************************")
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************************")
        print("Welcome to the E-Banking")
        print("*****************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdrawl")
        print("4.Exit")

        print("*****************************")
        choice = input("Enter your choice (1-4)  ")

        if choice =="1":
            show_balance(balance)
        elif choice =="2":
            balance+=deposit(balance)
        elif choice == "3":
            balance-=withdrawl(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*****************************")
            print("Not a valid choice")

    print("*****************************")
    print("Thanks for choosing us!")
    

if __name__ =='__main__':
    main()