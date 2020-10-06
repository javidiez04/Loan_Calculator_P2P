from sys import path
from sys import argv
path.append("../")
from LoanCalculatorFunction.LoanCalculator import interest_giver
if __name__== "__main__":
    interest_giver(int(argv[1]),argv[2])
