from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from common import *
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
async def main():
    return get_all_question()


@app.get('/receive/{id_student}/{result_student}/{id_question}')
async def receive(id_student, result_student, id_question):
    check_ans_and_update_row(id_student, result_student, id_question)
    return {'id_student': id_student, 'result_student': result_student, 'id_question': id_question}


templates = Jinja2Templates(directory="templates")


@app.get("/items")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
