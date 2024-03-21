import pandas as pd
from book import Book

def main():
    inputStop = False
    df = pd.DataFrame()
    while inputStop == False:
        inputMode = int(input("Select what you want to do (1 - add a book manually, 2 - import a .csv file, 3 - export csv, 4 - export database): "))
        if inputMode == 1:
            bookData = manualInput()
        elif inputMode == 2:
            break
        elif inputMode == 3:
            break
        elif inputMode == 4:
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

if __name__ == "__main__":
    main()