def main():
    n = int(input())
    a = set()
    for i in range(n):
        b = input().split()
        a = a.union(set(b))
    for x in a:
        print(x)


if __name__ == "__main__":
    main()
