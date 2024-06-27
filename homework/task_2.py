class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_data(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_data(self):
        return {
            'title': self.title,
            'year': self.year,
            'publisher': self.publisher,
            'genre': self.genre,
            'author': self.author,
            'price': self.price
        }

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


kniha = Book("Hobit", 1937, "George Allen & Unwin", "Fantasy", "J.R.R. Tolkien", 250)

print(kniha.get_data())

print(kniha.get_title())
print(kniha.get_year())
print(kniha.get_publisher())
print(kniha.get_genre())
print(kniha.get_author())
print(kniha.get_price())
