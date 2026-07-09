import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    b = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    x = [int(next(it)) for _ in range(m)]
    y = [int(next(it)) for _ in range(m)]

    length_type = {1: 1, 2: 2, 3: 4}
    points = {1: 1, 2: 3, 3: 5}

    # Проверка валидности трассы
    for i in range(n - 1):
        right1 = a[i] + length_type[b[i]]
        left2 = a[i + 1]
        if right1 >= left2:  # касание или пересечение
            print(0)
            return

    total = 0
    j = 0

    for i in range(n):
        start = a[i]
        end = start + length_type[b[i]]

        # Пропускаем прыжки, которые закончились до начала препятствия
        while j < m and x[j] + y[j] < start:
            j += 1

        if j == m:
            total -= 1
            continue

        if x[j] > start:
            # Прыжок начался позже начала препятствия
            total -= 1
            # Не двигаем j, т.к. этот прыжок может подойти для следующего
            continue

        # x[j] <= start
        if x[j] + y[j] >= end:
            # Успешно
            total += points[b[i]]
            # Не двигаем j, чтобы покрыть следующие препятствия
        else:
            # Не допрыгнул до конца
            total -= 1
            j += 1

    if total < 0:
        total = 0
    print(total)


if __name__ == "__main__":
    main()
