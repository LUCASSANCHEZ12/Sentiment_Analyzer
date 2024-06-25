from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import json
from typing import Dict, Any
import dill as pickle
import sys

sys.path.append("../model")
from Stopwords import filter_review

app = FastAPI()

#Allow CORS for communication with Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  #Changes based on frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model and the vectorizer
try:
    with open('./../model/model_1_en.pkl', 'rb') as fin:
        model_loaded = pickle.load(fin)
except FileNotFoundError:
    print("Error: 'model_1_en.pkl' not found.")

try:
    with open('./../model/vectorizer.pkl', 'rb') as fin:
        vectorizer = pickle.load(fin)
except FileNotFoundError:
    print("Error: 'vectorizer.pkl' not found.")


class Review(BaseModel):
    review: str

@app.get("/reviews", response_model=Dict[str, Any])
def get_all_reviews():
    
    # read the .json file
    with open('./reviews.json', 'r') as file:
        data = json.load(file)
    
    return data
@app.get("/reviews/{game_title}", response_model=Dict[str, Any])
def get_reviews(game_title: str):
    
    # read the .json file
    with open('./reviews.json', 'r') as file:
        data = json.load(file)
    
    # looking for the game un the .json file
    if game_title in data:
        return data[game_title]
    else:
        return HTTPException(status_code=404, detail="Game title not found")
    
# Helper function to filter and predict review
def get_prediction(text):
    processed_text = filter_review(text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model_loaded.predict(vectorized_text)[0]
    return int(prediction)  # Convert to int for JSON serialization 

# Endpoint to add a new review

@app.post("/reviews/{game_title}/add", response_model=Dict[str, Any])
def add_review(game_title: str, review: Review):
    try:
        # Read the JSON file
        with open('./reviews.json', 'r') as file:
            data = json.load(file)
            
        # Get the prediction for the new review
        review_text = review.review
        prediction = get_prediction(review_text)

        # Create a new review entry
        new_review_id = str(len(data.get(game_title, {}).get("reviews", {})) + 1)
        new_review = {
            "review": review_text,
            "value": prediction
        }

        # Add the new review to the existing reviews
        if game_title in data:
            data[game_title]["reviews"][new_review_id] = new_review
        else:
            data[game_title] = {"reviews": {new_review_id: new_review}}

        # Write the updated data back to the JSON file
        with open('./reviews.json', 'w') as file:
            json.dump(data, file, indent=4)

        return {"status": "success", "new_review_id": new_review_id, "prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))