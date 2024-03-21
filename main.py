import pandas as pd
from book import Book
from csvtool import convert_csv, add_row, output_csv

def main():
    inputStop = False
    df = pd.DataFrame(columns=["bookID","title","authors","average_rating","isbn","isbn13","language_code", "num_pages","ratings_count","text_reviews_count","publication_date","publisher"])
    while inputStop == False:
        inputMode = int(input("Select what you want to do (1 - add a book manually, 2 - import a .csv file, 3 - export csv, 4 - export database): "))
        if inputMode == 1:
            bookData = manualInput()
            df = add_row(df, bookData)
        elif inputMode == 2:
            df = convert_csv(df, "")
            break
        elif inputMode == 3:
            output_csv(df)
            print("saved to output/test.csv")
            break
        elif inputMode == 4:
            break
        elif inputMode == 0:
            inputStop = True
        
def manualInput():
    books = []
    headers = ["book_id","title","authors","average_rating","isbn","isbn13","language_code", "num_pages","ratings_count","text_reviews_count","publication_date","publisher"]
    headerData = []
    for header in headers:
        userInput = input(f"Please input {header}: ")
        headerData.append(userInput)
    book = Book(*headerData)  # Unpack headerData to pass individual attributes

    return headerData

if __name__ == "__main__":
    main()