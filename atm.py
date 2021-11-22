class atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    
    def checkbalance(self):
        print("You have $50,000 in your account")
    def withdraw(self, amount):
        newamount = 50000-amount
        print("You wihdrew $"+str(amount)+" from your bank account. You have $"+str(newamount)+" left")

def main():
    Card_Number = input("Enter your card number:")
    Pin_Number = input("Enter your pin number")

    new_user = atm(Card_Number, Pin_Number)
    print("Option 1: Check Account Balance")
    print("Option 2: Withdraw Money")
    activity=int(input("Choose your activity (type a number)"))

    if (activity==1):
        new_user.checkbalance()
    elif (activity==2):
        amount=input("Enter the amount you wish to withdraw")
        new_user.withdraw(amount)
    else:
        print("Enter a valid number")

if __name__=="__main__":
    main()