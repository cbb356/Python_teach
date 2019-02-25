class Book:

    def __init__(self, author="Unknown", title="Unknown", year="Unknown", genre="Unknown"):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, text):
        self.reviews.append(text)

    def __repr__(self):
        return "Book({}, {}, {}, {})".format(self.author, self.title, self.year, self.genre)
    def __str__(self):
        return "Book {}, {}, {}, {}\nReview: {}".format(self.author, self.title, self.year, self.genre, self.reviews)
    def __eq__(self, other):
        return self.author == other.author and self.title == other.title and self.year == other.year and self.genre == other.genre
    def __ne__(self, other):
        return self.author != other.author or self.title != other.title or self.year != other.year or self.genre != other.genre

class Review:
    def __init__(self, text):
        self.text = text

def main():
    b1 = Book("Simac", "Goblin Reservation", 1965, "Fiction")
    b2 = Book("Updike", "Run, Rabbit", 1956, "Drama")
    b3 = Book()
    b4 = b1
    books = [b1, b2]
    b1.add_review("Good")
    b1.add_review("Very good")
    b2.add_review("Not bad")

    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(books)
    print(b1 == b2)
    print(b1 == b4)



if __name__ == "__main__":
    main()
