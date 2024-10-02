def main():
    # Я пытался сам и у меня всё выглядело нормально, но эти грёбаные тесты не могут даже нормально объяснить, где и
    # почему им не нравятся границы таблички, а наугад работать как-то не захотелось
    size = int(input())
    ceil_width = int(input())

    string_length = size * ceil_width + (size - 1)

    for row in range(size):
        for column in range(size):
            print(f'{((row + 1) * (column + 1)): ^{ceil_width}}', end='')
            if column == size - 1:
                print()
            else:
                print('|', end='')
        if row + 1 != size:
            print('-' * string_length)


if __name__ == "__main__":
    main()
