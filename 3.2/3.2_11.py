def main():
    n = int(input())
    names = {}
    for i in range(n):
        s = input()
        if not (names.__contains__(s)):
            names[s] = 1
        else:
            names[s] += 1
    ans = 0
    for x in names:
        if names[x] > 1:
            ans += names[x]
    print(ans)


if __name__ == "__main__":
    main()
