def main():
    balance = 0

    while True:
        print("Your current balance is ${}".format(balance))
        print("1) Deposit money into account")
        print("2) Withdraw money from account")
        opt = int(input("Choose option: "))
        amount = int(input("Choose amount: "))

        if amount <= 0:
            raise ValueError("Must provide amount above $0!")

        if opt == 1:
            if balance + amount > 1000:
                print("Cannot exceed account limit of $1000!")
            else:
                balance += amount
        elif opt == 2:
            if balance - amount < 0:
                print("Cannot withdraw more than your current balance!")
            else:
                balance -= amount

if __name__ == '__main__':
    main()