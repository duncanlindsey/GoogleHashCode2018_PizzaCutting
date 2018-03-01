import numpy as np
import pandas as pd
import scipy

def import_data(filename):
    df = pd.read_csv(filename, delim_whitespace=True, header=None)
    return(df)

def extract_parameters(df):
    parameters = {}
    keys = ['R', 'C', 'L', 'H']
    values = df.iloc[0]
    for i in range(len(keys)):
        parameters[keys[i]] = values[i]
    return parameters

df = import_data('example.in')
parameters = extract_parameters(df)
print(parameters)