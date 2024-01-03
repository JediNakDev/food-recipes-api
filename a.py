import pandas as pd
import ast

# df = pd.read_csv("data34.csv")
# print(df.size)
# df1 = df.loc[0: 49999]

# df.to_csv("data5.csv", index=False)

df = pd.read_csv("data1.csv")
index = 5
name = df['name'][index]
description = df['description'][index]
minutes = int(df['minutes'][index])
tags_str = df['tags'][index]
nutrition_str = df['nutrition'][index]
steps_str = df['steps'][index]
ingredients_str = df['ingredients'][index]

tags = ast.literal_eval(tags_str)
nutrition = ast.literal_eval(nutrition_str)
steps = ast.literal_eval(steps_str)
ingredients = ast.literal_eval(ingredients_str)

print(description)
