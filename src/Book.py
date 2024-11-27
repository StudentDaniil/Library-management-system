class Book:
    def __init__(self, book_id, title, author, year, status="в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"ID: {self.book_id}\nНазвание: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}\nСтатус: {self.status}"