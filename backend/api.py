from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import json
from typing import Dict, Any


app = FastAPI()

#Allow CORS for communication with Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  #Changes based on frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df_training = pd.read_csv('./../dataset_training.csv')


class Review(BaseModel):
    review: str

@app.get("/reviews/{game_title}", response_model=Dict[str, Any])
def get_reviews(game_title: str):
    
    # read the .json file
    with open('backend\\reviews.json', 'r') as file:
        data = json.load(file)
    
    # looking for the game un the .json file
    if game_title in data:
        return data[game_title]
    else:
        return HTTPException(status_code=404, detail="Game title not found")