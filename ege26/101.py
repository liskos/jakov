def solve(filename):
    with open(filename) as f:
        n, k = map(int, f.readline().split())
        sizes = [int(f.readline()) for _ in range(n)]

    sizes.sort(reverse=True)  # сортируем по убыванию
    blocks = []  # каждый блок — это список вложенных контейнеров

    for size in sizes:
        placed = False
        for block in blocks:
            # можно ли положить контейнер в блок на верхний контейнер
            if block[-1] >= size + k:
                block.append(size)
                placed = True
                break
        if not placed:
            # создаём новый блок
            blocks.append([size])

    # минимальное количество ячеек — это количество блоков
    min_cells = len(blocks)
    # максимальный размер блока
    max_block_size = max(len(block) for block in blocks)

    print(min_cells, max_block_size)


solve("26data/26-101.txt")
