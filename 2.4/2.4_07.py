def main():
    n = int(input())
    k = 3
    for i in range(n):
        ls = k
        for j in range(k):
            print(f"До старта {ls} секунд(ы)")
            ls -= 1
        print(f"Старт {i + 1}!!!")
        k += 1


if __name__ == "__main__":
    main()
