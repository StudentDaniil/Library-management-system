import unittest

from src.Library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book("Book 1", "Author 1", "2022")
        self.library.add_book("Book 2", "Author 2", "2020")

    def tearDown(self):
        with open("books.json", "w") as file:
            file.write("")

    def test_add_book(self):
        initial_book_count = len(self.library.books)
        self.library.add_book("New Book", "New Author", "2023")
        new_book = self.library.books[-1]
        self.assertEqual(len(self.library.books), initial_book_count + 1)
        self.assertEqual(new_book.title, "New Book")

    def test_search_books(self):
        found_books = self.library.search_books("title", "Book 1")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].author, "Author 1")

    def test_remove_book(self):
        initial_book_count = len(self.library.books)
        existing_book_id = self.library.books[0].book_id
        self.library.remove_book(existing_book_id)
        self.assertEqual(len(self.library.books), initial_book_count - 1)

    def test_change_status(self):
        book_id = self.library.books[0].book_id
        self.library.change_status(book_id, "выдана")
        updated_book = next(b for b in self.library.books if b.book_id == book_id)
        self.assertEqual(updated_book.status, "выдана")


if __name__ == '__main__':
    unittest.main()
