import pandas as pd
from book import Book

def main():
    inputStop = False
    df = pd.DataFrame()
    while inputStop == False:
        inputMode = int(input("Select what you want to do (1 - add a book manually, 2 - import a .csv file, 3 - export csv, 4 - export database): "))
        if inputMode == 1:
            manualInput()
        elif inputMode == 2:
            break
        
def manualInput():
    books = []
    headers = ["book_id","title","authors","average_rating","isbn","isbn13","language_code", "num_pages","ratings_count","text_reviews_count","publication_date","publisher"]
    headerData = []
    for header in headers:
        userInput = input(f"Please input {header}: ")
        headerData.append(userInput)
    book = Book(*headerData)  # Unpack headerData to pass individual attributes
    books.append(book)
    books_data = []
    for book in books:
        books_data.append({
            "book_id": book.book_id,
            "title": book.title,
            "authors": book.authors,
            "average_rating": book.avg_rating,
            "isbn": book.isbn,
            "isbn13": book.isbn13,
            "language_code": book.language_code,
            "num_pages": book.num_pages,
            "ratings_count": book.ratings_count,
            "text_reviews_count": book.text_reviews_count,
            "publication_date": book.publication_date,
            "publisher": book.publisher
        })

if __name__ == "__main__":
    main()