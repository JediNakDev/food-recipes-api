import pandas as pd

df = pd.read_csv("data34.csv")
print(df.size)
df1 = df.loc[0: 49999]

df.to_csv("data5.csv", index=False)
