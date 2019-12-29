import pandas as pd

df = pd.read_excel('M25_1.xlsx')
#print(df.head())
#for v in df['identific']:
#    print(v)

print(df.loc[5,6])
