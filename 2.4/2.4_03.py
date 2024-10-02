def main():
    n = int(input())
    k = 1
    j = 0
    while k <= n:
        j += 1
        for i in range(j):
            if k <= n:
                print(k, end=" ")
            k += 1
        print()


if __name__ == "__main__":
    main()
