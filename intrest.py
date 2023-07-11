def compound_interest(principal, rate, time):
    return principal * (1 + rate/100)**time

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the number of years: "))

interest = compound_interest(principal, rate, time)

print("The compound interest is", interest)