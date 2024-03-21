class Book:
    def __init__(self, book_id, title, authors, avg_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.avg_rating = avg_rating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date = publication_date
        self.publisher = publisher

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthors: {', '.join(self.authors)}\nAverage Rating: {self.avg_rating}\nISBN: {self.isbn}\nISBN13: {self.isbn13}\nLanguage Code: {self.language_code}\nNumber of Pages: {self.num_pages}\nRatings Count: {self.ratings_count}\nText Reviews Count: {self.text_reviews_count}\nPublication Date: {self.publication_date}\nPublisher: {self.publisher}"