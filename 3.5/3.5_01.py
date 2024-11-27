from sys import stdin


def main():
    a = []
    for line in stdin:
        a += [int(i) for i in line.rstrip("\n").split()]
    print(sum(a))


if __name__ == "__main__":
    main()
