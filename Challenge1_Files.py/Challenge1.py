

from tkinter.tix import COLUMN

import csv
from pathlib import Path

from Python_Project.Python_functions import average_numbers



loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print("There total number of outstanding loans is: ", number_of_loans)

total_loan_cost = sum(loan_costs)
print("The total value of all loans in $ is: ", total_loan_cost)

average_loan_cost = total_loan_cost / number_of_loans
print("The average loan cost is: ", average_loan_cost)

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The future value of the loan is ${future_value: .2f}.")
print(f"The remaining months left on the loan are {remaining_months}.")

dicount_rate = 0.2

fair_value = future_value / (1 + (dicount_rate / 12)) ** remaining_months
print(f"The fair value of the loan is ${fair_value: .2f}.")

if fair_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth purchasing.")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def price_this_loan(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate)) ** remaining_months
    return present_value

present_value = price_this_loan(1000, 12, 0.2)
print(f"The present value of the loan is: {present_value: .2f}")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans = []

for row in loans:
    price = row["loan_price"]
    if price <= 500:
        inexpensive_loans.append(row)

print(inexpensive_loans)

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]


csvpath = Path("inexpensive_loans.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in inexpensive_loans:
        csvwriter.writerow(loan.values())

csvwriter.writerow(header)

output_path = Path("inexpensive_loans.csv")






