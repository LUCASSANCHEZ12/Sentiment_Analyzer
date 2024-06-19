from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd

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


reviews = df_training['review'].astype(str)

df_filtered = pd.DataFrame({
    'GameTitle': df_training['GameTitle'],
    'review': df_training['reviews'].astype(str),
    'voted_up': df_training['voted_up'].astype(int)
})

class Review(BaseModel):
    review: str

@app.get("/reviews/")
def get_reviews(game_title: str = Query(None), limit: int = 10):
    if game_title:
        filtered_df = df_filtered[df_filtered['GameTitle'].str.contains(game_title, case=False, na=False)]
        if filtered_df.empty:
            raise HTTPException(status_code=404, detail="Game title not found")
        return filtered_df.head(limit).to_dict(orient='records')
    return df_filtered.head(limit).to_dict(orient='records')