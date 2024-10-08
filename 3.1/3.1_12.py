def main():
    n = int(input())
    a = ("Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая")
    for i in range(n):
        print(a[i % 5])


if __name__ == "__main__":
    main()
