import pandas as pd
from book import Book

def main():
    #create empty data frame 
    df = pd.DataFrame()

    #start input loop
    inputStop = False
    while inputStop == False:
        inputMode = int(input("Select what you want to do (0 - Stop input, 1 - Add a book manually, 2 - Import a .csv file, 3 - Export csv, 4 - Export database): "))
        if inputMode == 1: #manual input
            manualInput()
        elif inputMode == 2: #input with csv file
            break
        elif inputMode == 3: #export csv file
            break
        elif inputMode == 4: #export database
            break
        elif inputMode == 0: #stop input loop
            inputStop = True 
        
def manualInput():
    books = [] #start empty list of book objects
    bookData = [] #information of a book
    headers = ["book_id","title","authors","average_rating","isbn","isbn13","language_code", "num_pages","ratings_count","text_reviews_count","publication_date","publisher"]
    for header in headers: #loop through headers list and input information about the book
        userInput = input(f"Please input {header}: ")
        bookData.append(userInput)
    book = Book(*bookData)  # Unpack headerData to pass individual attributes
    books.append(book) 
if __name__ == "__main__":
    main()