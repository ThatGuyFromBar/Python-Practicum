def main():
    s = input()
    cur = ""
    k = 0
    for i in range(len(s)):
        if s[i] != cur:
            if i != 0:
                print(cur, k)
            cur = s[i]
            k = 1
        else:
            k += 1
    print(cur, k)


if __name__ == "__main__":
    main()
