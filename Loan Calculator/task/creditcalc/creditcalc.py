import math
import argparse


def calculate_diff_payments(principal, periods, interest_rate):
    i = interest_rate / (12 * 100)  # Convert annual interest rate to monthly and percentage to decimal
    total_payment = 0
    for m in range(1, periods + 1):
        dm = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
        total_payment += dm
        print(f"Month {m}: payment is {dm}")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")


def calculate_annuity_payment(principal, periods, interest_rate):
    i = interest_rate / (12 * 100)
    annuity_payment = principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    return math.ceil(annuity_payment)


def calculate_principal(payment, periods, interest_rate):
    i = interest_rate / (12 * 100)
    principal = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    return round(principal)


def calculate_number_of_payments(principal, payment, interest_rate):
    i = interest_rate / (12 * 100)  # Convert annual interest rate to monthly and percentage to decimal
    n = math.log(payment / (payment - i * principal), 1 + i)
    total_months = math.ceil(n)
    overpayment = total_months * payment - principal
    return total_months, overpayment


def convert_months_to_years_months(total_months):
    years = total_months // 12
    months = total_months % 12
    if years > 0 and months > 0:
        return f"{years} {'year' if years == 1 else 'years'} and {months} {'month' if months == 1 else 'months'}"
    elif years > 0:
        return f"{years} {'year' if years == 1 else 'years'}"
    elif months > 0:
        return f"{months} {'month' if months == 1 else 'months'}"
    else:
        return "0 months"


def print_error_and_exit():
    print("Incorrect parameters")
    exit()


def main():
    parser = argparse.ArgumentParser(description="Loan Calculator")
    parser.add_argument("--type", help="Type of payment")  # Removed choices to handle manually
    parser.add_argument("--payment", type=float, help="Monthly payment amount")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--periods", type=int, help="Number of months needed to repay the loan")
    parser.add_argument("--interest", type=float, help="Annual interest rate (without percent sign)")
    args = parser.parse_args()

    # Verify interest included and no negative values for all args
    if not args.interest or args.interest < 0 or any(
            param for param in [args.payment, args.principal, args.periods] if param is not None and param < 0):
        print_error_and_exit()

    # Verify that type was provided and is either "diff" or "annuity"
    if not args.type or args.type not in ["diff", "annuity"]:
        print_error_and_exit()

    # Verify that if type == "diff", payment is not included
    if args.type == "diff" and args.payment:
        print_error_and_exit()

    if args.type == "diff":
        if not all([args.principal, args.periods]) or any(param < 0 for param in [args.principal, args.periods]):
            print_error_and_exit()
        calculate_diff_payments(args.principal, args.periods, args.interest)
    elif args.type == "annuity":
        if args.principal and args.periods and not args.payment:
            payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            print(f"Your monthly payment = {payment}!")
        elif args.payment and args.periods and not args.principal:
            principal = calculate_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {principal}!")
        elif args.principal and args.payment and not args.periods:
            periods, overpayment = calculate_number_of_payments(args.principal, args.payment, args.interest)
            years_months_str = convert_months_to_years_months(periods)
            print(f"It will take {years_months_str} to repay this loan!")
            print(f"Overpayment = {overpayment}")
        else:
            print_error_and_exit()
    else:
        print_error_and_exit()


if __name__ == "__main__":
    main()
