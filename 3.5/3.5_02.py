from sys import stdin


def main():
    a = []
    for line in stdin:
        b = line.rstrip("\n").split()
        a.append(int(b[2]) - int(b[1]))
    print(round(sum(a) / len(a)))


if __name__ == "__main__":
    main()
