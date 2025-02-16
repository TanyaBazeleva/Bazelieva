
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
tablesize = 2**32 - 1
table = {}

def hash(x):
    return x % tablesize

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global table
    table.clear()


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global table
    x = hash(author)
    if x not in table:
        table[x] = []
    for i in table[x]:
        if i[0] == author:
            i[1].add(title)
            return
    table[x].append((author, {title}))


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global table
    x = hash(author)
    if x in table:
        for i in table[x]:
            if i[0] == author:
                return title in i[1]
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global table
    x = hash(author)
    if x in table:
        for i in table[x]:
            if i[0] == author:
                i[1].discard(title)
                if not i[1]:
                    table[x].remove(i)
                    if not table[x]:
                        del table[x]
                return


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global table
    x = hash(author)
    if x in table:
        for i in table[x]:
            if i[0] == author:
                return sorted(i[1])
    return []
