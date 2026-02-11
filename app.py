from fastapi import FastAPI, HTTPException
from myproject.utils import json_to_dict_list
import os
from pathlib import Path

app = FastAPI(
    title="Scholl",
    description="Тестовое API для занятия, небольшая база студентов.",
    version="1.0",
    contact={"name": "Kirill", "email": "kirill.a.usanov#gmail.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
)

DATA = Path(__file__).resolve().parents[1] / "data" / "students.json"

app.openapi_tags = [
    {"name": "home", "description": "Приветсвие, начальная страница"},
    {"name": "students", "description": "Эндпоинты по студентам"},
]


@app.get(
    "/",
    tags=["home"],
    summary="Приветствие",
    description="Начальная страница",
)
def home_page():
    return {"message": "Привет, Мир!"}


@app.get(
    "/students",
    tags=["students"],
    summary="Список студентов",
    description="Вернёт всех учеников",
)
def get_all_students():
    try:
        return json_to_dict_list(DATA)

    except FileNotFoundError:
        raise HTTPException(500, "students.json not found")


@app.get(
    "/students/{grade}",
    tags=["students"],
    summary="Список студентов с фильтром по классу",
    description="Вернёт всех учеников в соответствии с параметром класса",
)
def get_stud_grade(grade: int):
    students = json_to_dict_list(DATA)
    if grade is not None:
        arr = []
        for i in students:
            if i["grade"] == grade:
                arr.append(i)
        return arr
