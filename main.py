from fastapi import FastAPI, HTTPException
from books_db import books_db
from pydantic import BaseModel

app = FastAPI()


class Base(BaseModel): ...


class Book(Base):
    isbn: str
    name: str


@app.get("/")
async def root():
    return {"message": "Hello my book list"}


@app.get("/books", response_model=list[Book])
async def get_books(count: int = 10, offset: int = 0):
    return books_db[offset : offset + count]


@app.get("/books/{isbn}")
async def get_books_by_id(isbn: str):
    for book in books_db:
        if book["isbn"] == isbn:
            return book

    raise HTTPException(status_code=404, detail="Книгу не знайдено")
