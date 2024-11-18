def main():
    s1 = input().split(", ")
    s2 = input().split(", ")
    for i in range(min(len(s1), len(s2))):
        print(f"{s1[i]} - {s2[i]}")


if __name__ == "__main__":
    main()
