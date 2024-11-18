from itertools import product, islice


def main():
    n = int(input())
    s = [x * y for x, y in product(range(1, n + 1), repeat=2)]
    for i in range(n):
        print(*islice(s, i * n, (i + 1) * n))


if __name__ == "__main__":
    main()
