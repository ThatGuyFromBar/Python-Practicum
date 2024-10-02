def main():
    n = int(input())
    print("А Б В")
    for a in range(n - 1):
        for b in range(n - 1):
            for c in range(n - 1):
                if a > 0 and b > 0 and c > 0 and (a + b + c) == n:
                    print(f"{a} {b} {c}")


if __name__ == "__main__":
    main()
