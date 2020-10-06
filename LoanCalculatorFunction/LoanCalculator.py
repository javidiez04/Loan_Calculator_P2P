import pandas as pd
import numpy as np

def interest_giver (y, x = "../Data/Zopa_data2.csv", update = False):
    x = pd.read_csv(x)

    #First we discard the values that are not regarded in the project

    if y < 1000 or y > 15000:
        return "The loan amount should be between 1000 and 15000"
    elif y % 100 != 0:
        return "The loan amount must be a multiple of 100"
    elif y > sum(x["Available"]):
        return "Your loan could not be processed, not enough funds"

    #Then we sort the rate values in the dataframe in order to have the lowest rates first
    #we also return the users that will be lending money in order of lowest to highest interest rate

    else:
        x = x.sort_values(by = "Rate")
        suma = 0
        i = 0
        while suma < y:
            suma += x.iloc[i,2]
            i += 1
        excess = suma - y
        ponderado = (x.iloc[i-1,2] - excess)*(x.iloc[i-1,1])
        for n in range(0,i-1):
            ponderado += x.iloc[n,1]*x.iloc[n,2]
        interest_rate = ponderado/y

    #next, we compute the weighted interest rate and the monthly and total payments

        rate = interest_rate*100
        interest_per_period = interest_rate/12
        denominador = ((1 + interest_per_period)**36)-1
        payment_per_month = y*((interest_per_period*(1 + interest_per_period)**36)/denominador)
        total_payment = payment_per_month*36

    #the last step is to programm the function so if the update parameter is set to true, the database
    #gets updated with the new data

        if update == True:
            x = x.reset_index()
            x.drop(range(0,i-1), inplace=True)
            x.drop("index", axis=1, inplace=True)
            x.iloc[0,2] = excess
            x.to_csv("../Data/Zopa_data2.csv", index = False)

        print( """
        Requested Amount: €{}
        Rate: {:.2f}%
        Monthly repayment: €{:.2f}
        Total repayment €{:.2f}""".format(y, rate, payment_per_month, total_payment))

def reset_database(x):
    if x == True:
        p = pd.read_csv("../Data/Zopa_data2Copy.csv")
        p.to_csv("../Data/Zopa_data2.csv", index=False)
