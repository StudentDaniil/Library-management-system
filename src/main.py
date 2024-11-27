from src.Library import Library

library = Library()

while True:
    print("\nМеню:")
    print("1.Добавить новую книгу")
    print("2.Удалить книгу")
    print("3.Поиск книги")
    print("4.Отобразить все книги")
    print("5.Изменить статус книги")
    print("6.Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания: ")
        library.add_book(title, author, year)
        print("\nКнига добавлена в библиотеку.")
    elif choice == '2':
        book_id = int(input("Введите ID книги для удаления: "))
        library.remove_book(book_id)

    elif choice == '3':
        search_key = input("Введите по какому параметру будем искать книгу (title, author, year): ")
        if search_key not in ('title', 'author', 'year'):
            print(f"\nТакого параметра нет, возврат в меню.")
            continue
        search_value = input("Введите название, автора или год выпуска книги: ")
        found_books = library.search_books(search_key, search_value)
        if found_books:
            for book in found_books:
                print(f'\n{book}')
        else:
            print(f"\nТакой книги нет.")
    elif choice == '4':
        books = library.load_books()

        if len(books) == 0:
            print(f"\nВ библиотеке нет книг.")
            continue
        print("\nКниги:")
        for book in books:
            print(f'\n{book}')
    elif choice == '5':
        book_id = int(input("Введите ID книги для изменения статуса: "))
        new_status = input("Введите новый статус (в наличии/выдана): ")
        if new_status not in ("в наличии", "выдана"):
            print(f'\nТакого статуса нет, возврат в меню.')
            continue
        library.change_status(book_id, new_status)
    elif choice == '6':
        print("\nДо свидания!")
        break
    else:
        print("\nНеверный ввод. Попробуйте снова.")
