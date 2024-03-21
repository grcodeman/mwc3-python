import pandas as pd
import csv

# headers = ["bookID","title","authors","average_rating","isbn","isbn13","language_code", "num_pages","ratings_count","text_reviews_count","publication_date","publisher"]

# this file will contain converting csv, updating datafram and then exporting csv

test_csv = pd.DataFrame(columns=["bookID","title","authors","average_rating","isbn","isbn13","language_code", "  num_pages","ratings_count","text_reviews_count","publication_date","publisher"])


# convert csv to dataframe
def convert_csv(df, path):
    # uses the traditional csv method to get the csv headers and removes any empty strings
    f = open('data/books.csv', 'r')
    reader = csv.reader(f)
    headers = next(reader)
    headers.remove("")

    # uses the pandas package to convert to a dataframe
    new = pd.read_csv(path, usecols=headers)

    df = pd.concat([df, new], ignore_index=True)
    print(df.columns)
    print(df.head(3))
    return df

#test_csv = convert_csv(test_csv, "data/books.csv")
#print(test_csv.columns)

# adds a line to the dataframe
def add_row(df, inputs):
    new_row = pd.DataFrame([inputs], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)

    return df


#test_csv = add_row(test_csv, ["211738","bruh","test","average_rating","isbn","isbn13","language_code", "num_pages","ratings_count","text_reviews_count","publication_date","publisher"])

# exports dataframe to a csv in output folder
def output_csv(df):
    new = df.to_csv("output/test.csv", sep=",", index=False)
    return new

#output_csv(test_csv)
