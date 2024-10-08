def main():
    s = input()
    a = s.split()
    n = int(input())
    for x in a:
        print(int(x) ** n, end=" ")


if __name__ == "__main__":
    main()
