def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    n = int(input())
    for x in a:
        print(x ** n)


if __name__ == "__main__":
    main()

