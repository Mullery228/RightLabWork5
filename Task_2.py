

def odd_nums(number: int) -> list:
    listik = list()
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for i in range(1, n + 1, 2):
        listik.append(i)
    return listik


n = 76
generator = odd_nums(n)
print(generator)
