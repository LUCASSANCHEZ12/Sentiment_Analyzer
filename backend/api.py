from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

#Allow CORS for communication with Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  #Changes based on frontend URL
    allow_credentials=True,


    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df_training = pd.read_csv('./../dataset_training.csv')


reviews = df_training['review'].astype(str)

df_filtered = pd.DataFrame(reviews, columns=['review'])
df_filtered['voted_up'] = df_training['voted_up'].astype(int)

class Review(BaseModel):
    review: str

@app.get("/reviews/")
def get_reviews():
    return df_filtered.to_dict(orient='records')