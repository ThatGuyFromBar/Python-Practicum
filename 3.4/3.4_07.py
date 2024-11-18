def main():
    s = []
    for i in range(int(input())):
        s.append(input())
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            print(f"{s[i]} - {s[j]}")


if __name__ == "__main__":
    main()
