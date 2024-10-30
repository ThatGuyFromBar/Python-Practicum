def main():
    ns = [int(input()) for i in range(int(input()))]
    print(max([ns[i] for i in range(1, len(ns)) if ns[i] - ns[i - 1] < ns[0]]))


if __name__ == "__main__":
    main()
