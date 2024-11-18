from itertools import product


def main():
    n = int(input())
    m = int(input())
    lens = len(str(n * m))
    for i, j in product(range(1, n + 1), range(1, m + 1)):
        print(f'{((i - 1) * m + j):>{lens}}', end=' ')
        if j == m:
            print()


if __name__ == "__main__":
    main()
