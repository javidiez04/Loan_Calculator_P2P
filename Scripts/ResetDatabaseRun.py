import sys
sys.path.append("../")
from LoanCalculatorFunction.LoanCalculator import reset_database
if __name__== '__main__':
    reset_database(sys.argv[1])
