def main():
    s = input().replace(" ", "").lower()
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
