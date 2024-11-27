import json
from typing import List

from src.Book import Book


class Library:
    """
        Класс Library представляет удобную систему для управления книгами.

        Атрибуты:
            books (List[Book]): Список объектов Book, представляющих книги в библиотеке.

        Методы:
            __init__(self): Конструктор для инициализации объекта Library загрузкой книг из 'books.json'.
            load_books(self) -> List[Book]: Загрузка данных о книгах из 'books.json'.
            save_books(self): Сохранение данных о книгах в 'books.json'.
            add_book(self, title: str, author: str, year: str): Добавление новой книги в библиотеку.
            search_books(self, search_type: str, keyword: str) -> List[Book]: Поиск книг по названию, автору или году.
            remove_book(self, book_id: int): Удаление книги из библиотеки по ID.
            change_status(self, book_id: int, new_status: str): Изменение статуса книги.
        """
    def __init__(self):
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        try:
            with open("books.json", "r") as file:
                try:
                    books_data = json.load(file)
                    books = []
                    if not books_data:
                        return []
                    for book_data in books_data:
                        book_id = book_data['id']
                        title = book_data['title']
                        author = book_data['author']
                        year = book_data['year']
                        status = book_data['status']
                        book = Book(book_id, title, author, year, status)
                        books.append(book)
                    return books
                except json.decoder.JSONDecodeError:
                    return []
        except FileNotFoundError:
            return []

    def save_books(self) -> None:
        books_data = []
        for book in self.books:
            book_data = {
                'id': book.book_id,
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'status': book.status
            }
            books_data.append(book_data)

        with open("books.json", "w") as file:
            json.dump(books_data, file, indent=4)

    def add_book(self, title: str, author: str, year: str) -> None:
        if not self.books:
            last_book_id = 0
        else:
            last_book_id = self.books[-1].book_id
        book_id = last_book_id + 1

        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def search_books(self, search_type: str, keyword: str) -> List:
        found_books = []
        for book in self.books:
            if search_type == "title" and book.title.lower() == keyword.lower():
                found_books.append(book)
            elif search_type == "author" and book.author.lower() == keyword.lower():
                found_books.append(book)
            elif search_type == "year" and str(book.year) == keyword:
                found_books.append(book)
        return found_books

    def remove_book(self, book_id: int) -> None:
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                print("\nКнига удалена.")
                return
        print("\nКнига с указанным ID не найдена.")

    def change_status(self, book_id: int, new_status: str) -> None:
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                self.save_books()
                print("\nСтатус книги изменен.")
                return
        print(f"\nКнига с указанным ID не найдена.")
