from itertools import product


def main():
    s = input()
    a = ["пик", "треф", "бубен", "червей"]
    a.remove(s)
    b = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    for i, j in product(b, a):
        print(i, j)


if __name__ == "__main__":
    main()
