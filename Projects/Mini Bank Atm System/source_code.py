class ATM:
    def __init__(self,balance = 0):
        self.balance = balance
    def check_balance(self):
        return f"Your balance is {self.balance}"
    def deposit(self,amount):
        self.balance += amount
        return f"Your new balance is {self.balance}"
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Collect Your Cash. Your new balance is {self.balance}"
        else:
            return "Insufficent balance. Withdrawal Failed."
def main():
    atm = ATM()
    while True:
        print("Welcome to Mini Bank ATM")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdrawl")
        print("4.Exit")
        
        choice = int(input("Enter Your Choice:"))
        
        if choice == 1:
            print(atm.check_balance())
        elif choice == 2:
            amount = float(input("Enter Amount to deposit:"))
            print(atm.deposit(amount))
        elif choice == 3:
            amount = float(input("Enter amount to withdraw:"))
            print(atm.withdraw(amount))
        elif choice == 4:
            print("Thank You For Using Mini Bank ATM System")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()