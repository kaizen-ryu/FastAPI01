"""
1.  Create a new API Endpoint that can
    fetch all books from a specific author
    using either Path Parameters or Query Parameters.
"""
from fastapi import FastAPI
app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

"""
using PATH parameter
"""

@app.get("/books/by_author/{author}")        #{} used to specify the parameter , author is the parameter name
async def read_book_by_author_using_path(author: str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    if books_to_return:
        return books_to_return
    return {"message": "anonymous author"}

"""
using QUERY parameter
"""

@app.get("/books/author")   # {} should not be used, even author is param name,
                            # it will work as query
                            # we can use anything instead of author as parameter
                            # when using query parameter
async def read_book_by_author_using_query(author: str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    if books_to_return:
        return books_to_return
    return {"message": "anonymous author"}