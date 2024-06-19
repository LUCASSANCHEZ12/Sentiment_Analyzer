from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Permitir CORS para la comunicación con el frontend de Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Cambia según la URL del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    description: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}