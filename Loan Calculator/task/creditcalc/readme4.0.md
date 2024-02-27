

# Loan Calculator

This Loan Calculator is a Python script designed to help users calculate various aspects of a loan including the annuity payment (monthly payment), the principal amount, and the number of payments (duration) required to repay the loan. It takes into account the annual interest rate and provides flexibility in terms of which parameters to input.

## Features

- Calculate the monthly payment required to repay the loan.
- Determine the principal amount of the loan.
- Compute the number of payments required to fully repay the loan.
- Convert the total number of payments into years and months for easier understanding.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.

## Installation

No installation is necessary. Just ensure you have Python 3.x installed and you can run the script directly from the command line.

## Usage

The loan calculator script can be executed from the command line with various arguments. Here are some examples of how to use the script:

- To calculate the monthly payment:
  ```
  python loan_calculator.py --principal=100000 --periods=60 --interest=4.5
  ```

- To find out the principal amount:
  ```
  python loan_calculator.py --payment=2200 --periods=60 --interest=4.5
  ```

- To determine how long it will take to repay the loan:
  ```
  python loan_calculator.py --principal=100000 --payment=2200 --interest=4.5
  ```

### Arguments

- `--payment`: The monthly payment amount.
- `--principal`: The loan principal amount.
- `--periods`: The number of months needed to repay the loan.
- `--interest`: The annual interest rate (without the percent sign).

**Note**: The interest rate is required for all calculations. You must provide at least two of the three parameters (payment, principal, periods) along with the interest rate for the script to perform a calculation.

## Contributing

Feel free to dive in! Open an issue, submit pull requests.

## License

This project is [MIT licensed](https://opensource.org/licenses/MIT).

---
