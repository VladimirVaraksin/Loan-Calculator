import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
message = "Incorrect parameters"

# Check for missing or invalid arguments
if (args.interest is None) or \
        (sum(1 for arg in vars(args).values() if arg is not None) < 4) or \
        any(arg < 0 for arg in vars(args).values() if isinstance(arg, (int, float))):
    print(message)
else:
    i = args.interest / (12 * 100)

    if args.type == "annuity":
        if args.periods is None:
            # No periods specified, calculate based on payment
            n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
            years = n // 12
            months = n % 12
            str_y = "" if years == 0 else (f"{years} year" if years == 1 else f"{years} years")
            str_m = "" if months == 0 else (f"and {months} month" if months == 1 else f"and {months} months")
            print(f"It will take {str_y} {str_m} to repay this loan!")
            overpayment = args.payment * n - args.principal
            print(f"Overpayment = {overpayment}")
        elif args.payment is None:
            # No payment specified, calculate based on periods
            p = math.ceil(args.principal * (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
            print(f"Your annuity payment = {p}!")
            overpayment = p * args.periods - args.principal
            print(f"Overpayment = {overpayment}")
        else:
            # Calculate principal if payment is provided
            p = math.floor(args.payment / (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
            print(f"Your loan principal = {p}!")
            overpayment = args.payment * args.periods - p
            print(f"Overpayment = {overpayment}")
    elif args.type == "diff":
        if args.payment is not None:
            print(message)
        else:
            sum_payments = 0
            for x in range(1, args.periods + 1):
                dm = math.ceil(
                    args.principal / args.periods + i * (args.principal - args.principal * (x - 1) / args.periods))
                print(f"Month {x}: payment is {dm}")
                sum_payments += dm
            overpayment = sum_payments - args.principal
            print(f"\nOverpayment = {overpayment}")
    else:
        print(message)
