from itertools import cycle, islice


def main():
    dishes = [input() for i in range(int(input()))]
    days = int(input())
    print('\n'.join(islice(cycle(dishes), days)))


if __name__ == "__main__":
    main()
