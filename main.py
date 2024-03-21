import pandas as pd
from book import Book

def main():
    #create empty data frame 
    df = pd.DataFrame()

    #start input loop
    inputStop = False
    while inputStop == False:
        inputMode = int(input("Select what you want to do (1 - add a book manually, 2 - import a .csv file, 3 - export csv, 4 - export database): "))
        if inputMode == 1: #manual input
            bookData = manualInput()
        elif inputMode == 2: #input with csv file
            break
        elif inputMode == 3: #export csv file
            break
        elif inputMode == 4: #export database
            break
        elif inputMode == 0: #stop input loop
            inputStop = True 
        
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