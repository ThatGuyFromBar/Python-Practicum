def main():
    n = input()
    for i in range(0, 10, 2):
        n = n.replace(str(i), "")
    print(n)


if __name__ == "__main__":
    main()
