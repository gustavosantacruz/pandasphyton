import pandas as pd

path = 'SuperMarket Analysis.csv'

retail_data = pd.read_csv(path, encoding='latin1')

print(type(retail_data))

print(retail_data)