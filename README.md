# Loan Calculator

A simple Python-based loan calculator that supports both **Annuity** and **Differentiated** payment plans. This tool helps you calculate key loan parameters like monthly payments, total interest paid, and overpayment based on user-provided inputs.

## Features

- **Annuity Payments**: Calculate the monthly payment, loan principal, number of periods, or interest rate.
- **Differentiated Payments**: Calculate the monthly differentiated payment and the total overpayment.

## Usage

To use the loan calculator, run the script `creditcalc.py` with the necessary parameters. You must provide the `--type` (either "annuity" or "diff") and `--interest` (annual interest rate as a percentage). Then, based on the type of loan, you need to specify the required parameters.

### Annuity Payments

For **annuity** loans, provide a combination of any two of the following parameters:
- `principal`: The total loan amount (in your currency).
- `periods`: The number of months (loan duration).
- `payment`: The fixed monthly payment amount.

The missing parameter will be calculated and outputted.

### Differentiated Payments

For **differentiated** loans, you need to provide:
- `principal`: The total loan amount.
- `periods`: The number of months (loan duration).

The program will calculate the **differentiated monthly payments** and the **total overpayment**.

### Output

The program will output the following based on your inputs:
- For **Annuity**: the missing parameter (either `principal`, `periods`, or `payment`) and the total overpayment.
- For **Differentiated**: the list of monthly differentiated payments and the total overpayment.
