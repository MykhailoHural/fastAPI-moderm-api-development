from fastapi import APIRouter, HTTPException
from books_db import books_db
from schemas.books import Book
router = APIRouter()


@router.get("/", response_model=list[Book])
async def get_books(count: int = 10, offset: int = 0):
    return books_db[offset : offset + count]


@router.get("/{isbn}", response_model=Book)
async def get_books_by_id(isbn: str):
    for book in books_db:
        if book["isbn"] == isbn:
            return book

    raise HTTPException(status_code=404, detail="Книгу не знайдено")


@router.post("/")
async def post_book(book: Book) -> Book:
    book_record = book.model_dump()
    books_db.append(book_record)
    return book
