import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('./data/GalaxyData.csv')

df_no_na = df.dropna()

print(df.shape)
print(df_no_na.shape)