
def main():
    with open(input(), encoding='UTF-8') as base_text:
        numbers = [int(number) for number in base_text.read().split()]
    print(len(numbers))
    pos = [x for x in numbers if x > 0]
    print(len(pos))
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    print(round(sum(numbers) / len(numbers), 2))


if __name__ == "__main__":
    main()
