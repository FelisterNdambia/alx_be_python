# finance_calculator.py

# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
total_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - total_expenses

# Project Annual Savings
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")


