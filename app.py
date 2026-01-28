from fastapi import FastAPI, HTTPException
from myproject.utils import json_to_dict_list
import os
from pathlib import Path

app = FastAPI()

DATA = Path(__file__).resolve().parents[1] /"data"/"students.json"


@app.get("/")
def home_page():
    return {"message": "Привет, Мир!"}


@app.get("/students")
def get_all_students():
    try:
        return json_to_dict_list(DATA)

    except FileNotFoundError:
        raise HTTPException(500, "students.json not found")


@app.get("/students/{grade}")
def get_stud_grade(grade: int):
    students = json_to_dict_list(DATA)
    if grade is not None:
        arr = []
        for i in students:
            if i["grade"] == grade:
                arr.append(i)
        return arr
