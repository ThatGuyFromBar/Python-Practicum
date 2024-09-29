def main():
    n = int(input())
    good = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            good = False
            break
    if n == 1:
        good = False
    if good:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
