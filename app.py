from fastapi import FastAPI, HTTPException 
from myproject.utils import json_to_dict_list 
import os 
from pathlib import Path 

DATA = Path(__file__).resolve().parents[2] / "data" / "students.json" 

app = FastAPI() 

@app.get("/") 
def home_page(): 
    return {"message": "Привет, Мир!"} 

@app.get("/students") 
def get_all_students(): 
    try: 
        return json_to_dict_list(DATA) 
    
    except FileNotFoundError: 
        raise HTTPException(500, "students.json not found") 