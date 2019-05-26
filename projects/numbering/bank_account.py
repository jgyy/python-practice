"""
Bank Account Manager - Create a class called Account which will be an abstract class for three
other classes called CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and
debits from these accounts through an ATM style program.
"""


class Account:
    """Account Class"""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_customer(self):
        """Display Amount"""
        print(self.customer_id)

    def get_customer(self):
        """:return:"""
        return self.customer_id


class CheckingAccount(Account):
    """Checking Account Class"""
    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.num_str = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.num_str[:self.num_str.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.num_str[self.num_str.find('.') + 1:])

    def deposit(self, deposit_amount):
        """:param deposit_amount:"""
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        """
        :param withdraw_amount: separates the whole number from decimal number of the amount to
        withdraw
        """
        # debugging purposes only
        print("self whole", self.amount_whole)
        print("self part", self.amount_part)

        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        num_str = str(withdraw_amount)
        self.withdraw_part = int(num_str[num_str.find('.') + 1:])

        # debugging purposes only
        print("whole", self.withdraw_whole)
        print("part", self.withdraw_part)

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal value of requested amount is greater than the
            # decimal value of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # debugging purposes only
            print("\nnew whole", self.amount_whole)
            print("new part", self.amount_part)
            print("new amount", new_amount)

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        """Display Amount"""
        print(self.amount)

    def get_amount(self):
        """:return:"""
        return self.amount


class SavingsAccount(Account):
    """Savings Amount Class"""
    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.num_str = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.num_str[:self.num_str.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.num_str[self.num_str.find('.') + 1:])

    def deposit(self, deposit_amount):
        """
        :param deposit_amount:
        """
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        """
        :param withdraw_amount: separates the whole number from decimal number of the amount to
        withdraw
        """
        # debugging purposes only
        print("self whole", self.amount_whole)
        print("self part", self.amount_part)

        # separates the whole number from decimal number of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        num_str = str(withdraw_amount)
        self.withdraw_part = int(num_str[num_str.find('.') + 1:])

        # debugging purposes only
        print("whole", self.withdraw_whole)
        print("part", self.withdraw_part)

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal value of requested amount is greater than the
            # decimal value of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # debugging purposes only
            print("\nnew whole", self.amount_whole)
            print("new part", self.amount_part)
            print("new amount", new_amount)

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        """Display Amount"""
        print(self.amount)

    def get_amount(self):
        """:return: amount"""
        return self.amount


class BusinessAccount(Account):
    """Business Account Class"""
    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.num_str = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.num_str[:self.num_str.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.num_str[self.num_str.find('.') + 1:])

    def deposit(self, deposit_amount):
        """
        :param deposit_amount:
        """
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        """
        :param withdraw_amount: separates the whole number from decimal number of the amount to
        withdraw
        """
        # debugging purposes only
        print("self whole", self.amount_whole)
        print("self part", self.amount_part)

        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        num_str = str(withdraw_amount)
        self.withdraw_part = int(num_str[num_str.find('.') + 1:])

        # debugging purposes only
        print("whole", self.withdraw_whole)
        print("part", self.withdraw_part)

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal value of requested amount is greater than the
            # decimal value of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # debugging purposes only
            print("\nnew whole", self.amount_whole)
            print("new part", self.amount_part)
            print("new amount", new_amount)

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        """Display Amount"""
        print(self.amount)

    def get_amount(self):
        """:return: amount"""
        return self.amount


if __name__ == '__main__':
    IS_SESSION_ON = True
    IS_CUSTOMER = False

    def initialise_objects():
        """initialise objects"""

        sally_checking = CheckingAccount(1, 2567.50)
        paolo_savings = SavingsAccount(2, 12890.01)
        paolo_business = BusinessAccount(2, 14500.40)

        return [[sally_checking, 1, 1], [paolo_savings, 2, 2], [paolo_business, 2, 3]]

    MASTER_LIST = initialise_objects()

    while IS_SESSION_ON is True:
        print("Welcome to 24-hour ATM service.")
        print("Insert your card.")

        # Card reading the customer info representation
        CUSTOMER_ID = input("Enter your customer id number: ")
        print("\n")

        CUSTOMER_ACCOUNTS = []
        for i in MASTER_LIST:
            if i[1] == CUSTOMER_ID:
                CUSTOMER_ACCOUNTS.append(i[2])
                IS_CUSTOMER = True

        if IS_CUSTOMER is True:
            IS_ACCOUNT_SELECTED = False

            while IS_ACCOUNT_SELECTED is False:
                print("Enter 1 for checking account")
                print("Enter 2 for savings account")
                print("Enter 3 for business account")
                ACCOUNT_TYPE = input("Enter which account to use: ")
                OBJECT_NAME = ''
                if ACCOUNT_TYPE in CUSTOMER_ACCOUNTS:
                    for x in MASTER_LIST:
                        if ACCOUNT_TYPE == x[2]:
                            OBJECT_NAME = x[0]

                    IS_ACCOUNT_SELECTED = True
                    IS_ACCOUNT_SESSION_ON = True

                    while IS_ACCOUNT_SESSION_ON is True:
                        print("\nHow may I help you?")
                        print("Press 1 for balance view.")
                        print("Press 2 for withdrawals")
                        print("Press 3 to exit.")

                        ACTION_VALUE = input("Please enter your choice: ")

                        if ACTION_VALUE == 1:
                            OBJECT_NAME.display_amount()
                            print("\n")

                        if ACTION_VALUE == 2:
                            AMOUNT_TO_WITHDRAW = input("Enter the amount to withdraw: ")
                            TEMP_STR = str(AMOUNT_TO_WITHDRAW)

                            ADJUSTED_AMOUNT = "%.2f" % AMOUNT_TO_WITHDRAW
                            print("adjusted_amount:", ADJUSTED_AMOUNT)
                            OBJECT_NAME.withdraw(ADJUSTED_AMOUNT)

                            print("current balance is", OBJECT_NAME.get_amount())
                            print("\n")

                        if ACTION_VALUE == 3:
                            IS_ACCOUNT_SESSION_ON = False
                            print("Thank for using the 24-hour ATM service.")
                            print("Have a pleasant day.")
                            print("\n\n")
                            print("##########################################")
                else:
                    print("Error. You don't have that account.")
                    print("Please try again.\n")

        else:
            print("Cannot find your record.")
            print("Please get your card.")
            print("Exiting this session...")
