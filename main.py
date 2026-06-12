from fastapi import FastAPI
from routers import books

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello my book list"}


app.include_router(books.router, prefix="/books")
