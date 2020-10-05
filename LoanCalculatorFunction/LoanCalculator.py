import pandas as pd
import numpy as np

def interest_giver (x,y):
    if y < 1000 or y > 15000:
        return "The loan amount should be between 1000 and 15000"
    elif y % 100 != 0:
        return "The loan amount must be a multiple of 100"
    elif y > sum(x["Available"]):
        return "Your loan could not be processed, not enough funds"
    else:
        min_rate = min(x["Rate"])
        x = x.sort_values(by = "Rate")
        suma = 0
        i = 0
        rates = []
        while suma < y:
            suma += x.iloc[i,2]
            rates.append(x.iloc[i,1])
            i += 1
        excess = suma - y
        ponderado = (x.iloc[i-1,2] - excess)*(x.iloc[i-1,1])
        for n in range(0,i-1):
            ponderado += x.iloc[n,1]*x.iloc[n,2]
        interest_rate = ponderado/y
        return interest_rate
