"""**Mortgage Calculator** -
Calculate the monthly payments of a fixed term mortgage
over given Nth terms at a given interest rate. Also figure
out how long it will take the user to pay back the loan."""
if __name__ == '__main__':
    MONTHS = int(input("Enter mortgage term (in months): "))
    RATE = float(input("Enter interest rate: "))
    LOAN = float(input("Enter loan value: "))

    MONTHLY_RATE = RATE / 100 / 12
    PAYMENT = (MONTHLY_RATE / (1 - (1 + MONTHLY_RATE) ** (-MONTHS))) * LOAN

    print("Monthly payment for a $%.2f %s year mortgage at %.2f%% interest rate is: $%.2f"
          % (LOAN, (MONTHS / 12), RATE, PAYMENT))
