import requests
import datetime

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Class for accessing data from the qotd (Quote of the Day) website
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class ATM():
    # Method - inializer for the qotd site class
    def __init__(self, starting_balance=0, irate=0.001):
        self.account_balance = starting_balance
        self.irate = irate
        self.transactions = []
        self.last_date_icomputed = None

    
    # Method - returns the account balance
    def balance(self):
        return self.account_balance
    
    # Method - deposits the given amount in the account
    def deposit(self, amount):
        self.account_balance += amount
        self.transactions.append(f'user deposited ${amount}')

    # Method - returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if self.account_balance - amount > 0:
            return True
        return False

    # Method - withdraws the amount from the account and returns it
    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.account_balance -= amount
            self.transactions.append(f'user withdrew ${amount}')
            return amount
        else:
            return 0

    # Method - returns the amount of interest calculated on the account
    def calc_interest(self):
        if self.last_date_icomputed == None:
            self.last_date_icomputed = True
            return self.account_balance * self.irate
        return 0.0

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Function and code for Lab 18 version 1
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Function - for the lab17 coding exercise which provides the version 1 output
def lab18_verion1():
    atm = ATM() # create an instance of our class
    print('Welcome to the ATM')
    while True:
        command = input('Enter a command: ')
        if command in ['balance', 'b']:
            balance = atm.balance() # call the balance() method
            print(f'Your balance is ${balance}')
        elif command in ['deposit', 'd']:
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount) # call the deposit(amount) method
            print(f'Deposited ${amount}')
        elif command in ['withdraw', 'w']:
            amount = float(input('How much would you like '))
            if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
                atm.withdraw(amount) # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
                print(f'New Balance ${atm.balance()}')
            else:
                print('Insufficient funds')
        elif command in ['interest', 'i']:
            amount = atm.calc_interest() # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')
        elif command in ['transactions', 't']:
            atm.print_transactions()
        elif command in ['help', 'h']:
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('exit     - exit the program')
        elif command in ['exit', 'e', 'quit', 'q']:
            break
        else:
            print('Command not recognized')


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Function and code for Lab 18 version 2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Function - for the lab17 coding exercise which provides the version 2 output
def lab18_verion2():
    pass

         

# Function - Main processing function where you can easily set what version of the code you want to utilize
def main():

    print("\n\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-") 
    lab18_verion1()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n\n")

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    lab18_verion2()


# Execute the main() function
main()