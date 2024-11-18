from itertools import combinations


def main():
    n = int(input())
    print("А Б В")
    for i, j in list(combinations(range(1, n), 2)):
        print(f"{i} {j - i} {n - j}")


if __name__ == "__main__":
    main()
