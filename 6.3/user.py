
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
keys = []
values = []
tablesize = 2**32 - 1

def hash(x):
    return x % tablesize

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global keys, values
    for i in range(tablesize):
        keys.append(None)
        values.append(None)


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global keys, values
    x = hash(author)
    while keys[x] is not None:
        if keys[x] == author:
            values[x].add(title)
            return
        x = (x + 1) % tablesize
    keys[x] = author
    values[x] = {title}


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global keys, values
    x = hash(author)
    while keys[x] is not None:
        if keys[x] == author:
            return title in values[x]
        x = (x + 1) % tablesize
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global keys, values
    x = hash(author)
    while keys[x] is not None:
        if keys[x] == author:
            values[x].discard(title)
            if not values[x]:
                keys[x] = None
                values[x] = None
            return
        x = (x + 1) % tablesize


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global keys, values
    x = hash(author)
    while keys[x] is not None:
        if keys[x] == author:
            return sorted(values[x])
        x = (x + 1) % tablesize
    return []
