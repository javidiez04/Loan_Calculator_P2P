import sys
sys.path.append("../")
from Tests.FunctionTest import test_interest_giver
from LoanCalculatorFunction.LoanCalculator import interest_giver
if __name__== '__main__':
    test_interest_giver()
    print("Everything passed")
