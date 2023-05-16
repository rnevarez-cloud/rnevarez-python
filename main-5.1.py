interest_rate = int(input("Please enter the interest rate. Note: Please enter the rate as a whole number. For example, if the rate is 8%, then enter 8:"))
print()

initial_investment = float(input("Please enter the initial investment. Please enter the investment as a whole number. For example, if the initial investment is $10,000, then enter 10000:"))

interest_rate = interest_rate * .01

double_investment = initial_investment * 2

year = 0

while initial_investment <= (double_investment) :
  year += 1
  initial_investment = ((interest_rate * initial_investment) + initial_investment)
  print(f"Year {year} - Investment Amount: ${round(initial_investment,2)}")
