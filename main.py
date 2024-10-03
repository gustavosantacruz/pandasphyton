import pandas as pd

path = 'online_retail.csv'

retail_data = pd.read_csv(path, encoding='latin1')

print(type(retail_data))

print(retail_data)
