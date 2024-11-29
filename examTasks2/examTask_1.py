def main():
    n = int(input())
    answer = []
    for i in range(n):
        package = input().split('&')
        s = ''.join([package[2][i] for i in range(int(package[0]), len(package[2]), 2)])[:int(package[1])]
        answer.append(s)
    for x in answer:
        print(x)


if __name__ == "__main__":
    main()
