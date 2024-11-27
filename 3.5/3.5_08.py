
def main():
    with open(input(), encoding='UTF-8') as base_text:
        words1 = set([word for word in base_text.read().split()])
    with open(input(), encoding='UTF-8') as base_text:
        words2 = set([word for word in base_text.read().split()])
    unique_words = words1 ^ words2
    with open(input(), 'w', encoding='UTF-8') as finished_text:
        print('\n'.join(sorted(unique_words)), file=finished_text)


if __name__ == "__main__":
    main()
