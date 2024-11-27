
def main():
    text = []
    with open(input(), encoding='UTF-8') as base_text:
        for line in base_text:
            text.append(line)
    k = int(input()) + 1
    for i in range(1, k):
        print(text[len(text) - (k - i)].strip())


if __name__ == "__main__":
    main()
