def main():
    a, b, c = [float(i) for i in input().split()]
    while a <= b:
        print(f"{a:.2f}")
        a += c


if __name__ == "__main__":
    main()
