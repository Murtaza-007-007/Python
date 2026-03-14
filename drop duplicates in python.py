
#Drop Duplicates in python


import pandas as pd

your_data=[1,1,22,22,33,33,44,44,55,55]

df=pd.DataFrame(your_data)
print(df)

df.drop_duplicates(inplace=True)
print(df)

