while True:
    amount_loan = int(input("\n\nEnter amount of the loan (Principal)? "))
    interest_rate_per_year = int(input("Enter intertest rate per year (percent)? "))
    num_year = int(input("Enter number of years? "))

    num_month = (num_year * 12)
    interest_per_month = (interest_rate_per_year / 12) / 100
    p = (1  + interest_per_month) ** num_month
    q = (interest_per_month * p) / (p - 1)
    monthly_payment = amount_loan *  q

    print(f"\n\nThe amount of the loan (principal): {amount_loan:.2f}")
    print(f"Interest rate/year (percentage): {interest_rate_per_year:.1f}%")
    print(f"Interest rate/month (decimal): {interest_per_month:.6f}")
    print(f"Number of years: {num_year}")
    print(f"Number of months: {num_month}")
    print(f"Monthly payment: {monthly_payment:.2f}")

    print("\n\nMonth\tOld Balance\tMonthly Payment\tInterest Paid\tPrincipal Paid\tNew Balance")
    print("------------------------------------------------------------------------------------")
    for month in range(1, num_month + 1):
        interest_paid = amount_loan * interest_per_month
        principal_paid = monthly_payment - interest_paid
        new_balance = amount_loan - principal_paid
        format_new_balance = abs(new_balance)

        print(f"{month}\t{amount_loan:.2f}\t\t{monthly_payment:.2f}\t\t{interest_paid:.2f}\t\t{principal_paid:.2f}\t\t{abs(format_new_balance):.2f}")

        amount_loan = format_new_balance