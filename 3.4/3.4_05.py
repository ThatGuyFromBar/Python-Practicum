def main():
    s = []
    for i in range(3):
        t = input().split(", ")
        for x in t:
            s.append(x)
    s.sort()
    for i in range(len(s)):
        print(f"{i + 1}. {s[i]}")


if __name__ == "__main__":
    main()
