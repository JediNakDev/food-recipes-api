import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hi, this is Food Recipes API"}


@app.get("/food-recipe/{index}")
def get_food_recips(index: int):
    if index < 50000:
        df = pd.read_csv("data1.csv")
    elif index < 100000:
        df = pd.read_csv("data2.csv")
        index = index - 50000
    elif index < 150000:
        df = pd.read_csv("data3.csv")
        index = index - 100000
    elif index < 200000:
        df = pd.read_csv("data4.csv")
        index = index - 150000
    else:
        df = pd.read_csv("data5.csv")
        index = index - 200000
    name = df['name'][index]
    description = df['description'][index]
    minutes = int(df['minutes'][index])
    tags = df['tags'][index]
    nutrition = df['nutrition'][index]
    steps = df['steps'][index]
    ingredients = df['ingredients'][index]
    return {
        "name": name,
        "description": description,
        "minutes": minutes,
        "tags": tags,
        "nutrition": nutrition,
        "steps": steps,
        "ingredients": ingredients
    }
