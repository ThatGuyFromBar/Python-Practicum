def main():
    a = int(input())
    b = int(input())
    print(a, end=" ")
    while a != b:
        if a < b:
            a += 1
        else:
            a -= 1
        print(a, end=" ")


if __name__ == "__main__":
    main()
