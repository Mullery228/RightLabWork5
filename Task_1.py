import sys
def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for i in range(1, n + 1, 2):
        yield i


n = 76
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
