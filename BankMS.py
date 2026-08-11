class InsufficientBalanceError(Exception):
    print("you have not sufficient Balance")

class BankAccount:
    def __init__(self,Accountnumber,AccountHoldername,Balance):
        self.Account_number=Accountnumber
        self.Account_Holder_name=AccountHoldername
        self.__Balance=Balance
        self.Transaction_History=[]
    
    def deposit(self):
        amount = float(input("Enter the amount to deposite:"))
        if amount <= 0:
            raise ValueError("Amount must be greatar than zero")
        self.__Balance +=amount
        self.Transaction_History.append(f"deposited:{amount}")
        with open("tranactions.txt","a") as file:
            file.write(f"Deposited $:{amount}\n")
        print("amount deposited successfully")


    def withdraw(self):
        amount=float(input("Enter the amount to withdraw:"))
        if amount<=0:
            raise ValueError("Amount must be greater than zero")
        if amount >self.__Balance:
            raise InsufficientBalanceError("You not sufficient balance")
        self.__Balance -=amount
        self.Transaction_History.append(F"withdraw:{amount}")
        with open("transaction.txt","w") as file:
            file.write(f"Withdraw $:{amount}\n")
        print("withdraw succesffully")

    def check_balance(self):
        print(f"current balance:{self.__Balance}")

    
    def show_transaction_history(self):
        print(self.Transaction_History)

    @staticmethod
    def Menu():
        print("====MENU====")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.check balance")
        print("4.Transaction History")
        print("5.Exit")

    def   loop(self):
        while True:
            self.Menu()
            user=int(input("Enter the Sr no of want to do:"))
            if user==1:
                try:
                    self.deposit()
                except ValueError as e:
                    print(e)

            if user==2:
                try:
                   self.withdraw()
                except ValueError as e:
                    print(e)
                except InsufficientBalanceError as i:
                    print(i)

            if user==3:
                self.check_balance()
            if user==4:
                self.show_transaction_history( )

            if user==5:
                print("thank you ")
                break

Bank=BankAccount(1231241212,"shubham",10000)
Bank.loop()