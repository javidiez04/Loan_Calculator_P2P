from LoanCalculatorFunction.LoanCalculator import interest_giver

def test_interest_giver():
    assert interest_giver(1000) == 5.8031, "Interest Rate Should be 5.8031 & the Monthly Payment €30.89"
