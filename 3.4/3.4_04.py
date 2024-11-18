def main():
    s = input().split()
    for i in range(len(s)):
        print(" ".join([s[x] for x in range(i + 1)]))


if __name__ == "__main__":
    main()
