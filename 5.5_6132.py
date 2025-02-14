# https://basecamp.eolymp.com/uk/problems/6132
# task 5.5
import sys


def count_workers(arrival_times, max_time):
    """ Функція підраховує кількість робітників, які встигли прийти до max_time. """
    left, right = 0, len(arrival_times)
    while left < right:
        mid = (left + right) // 2
        if arrival_times[mid] <= max_time:
            left = mid + 1
        else:
            right = mid
    return left


def can_fill_bus(delay, n, m, stops):
    """ Перевіряє, чи можна перевезти max_workers за певний час із затримкою delay. """
    workers_on_bus = 0
    bus_time = delay  # Початковий час виїзду автобуса

    for i in range(n):
        travel_time, k, *arrival_times = stops[i]
        arrival_times.sort()  # Впорядковуємо за часом приходу

        # Визначаємо, скільки людей прийде до моменту bus_time
        count = count_workers(arrival_times, bus_time)

        # Скільки місць залишилось
        available_space = min(m - workers_on_bus, count)
        workers_on_bus += available_space

        # Якщо автобус заповнився — виходимо
        if workers_on_bus == m:
            return True

        # Оновлюємо час автобуса після руху до наступної зупинки
        bus_time += travel_time

    return workers_on_bus == m


def find_min_time(n, m, stops):
    """ Основна функція пошуку мінімального часу. """
    left, right = 0, max(max(stops[i][2:]) for i in range(n))
    while left < right:
        mid = (left + right) // 2
        if can_fill_bus(mid, n, m, stops):
            right = mid
        else:
            left = mid + 1
    return left


# Зчитування вхідних даних
n, m = map(int, sys.stdin.readline().split())
stops = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(find_min_time(n, m, stops) + sum([stop[0] for stop in stops]))


