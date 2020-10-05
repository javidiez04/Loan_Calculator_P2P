import sys
sys.path.append("../")
from LoanCalculatorFunction.LoanCalculator import interest_giver
if __name__== '__main__':
    interest_giver(int(sys.argv[1]))
