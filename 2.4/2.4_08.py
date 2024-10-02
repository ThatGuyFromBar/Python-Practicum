def main():
    n = int(input())
    winner = ""
    maxn = 0
    for i in range(n):
        s1 = input()
        s2 = input()
        s = 0
        for j in range(len(s2)):
            s += int(s2[j])
        if s >= maxn:
            maxn = s
            winner = s1
    print(winner)


if __name__ == "__main__":
    main()
