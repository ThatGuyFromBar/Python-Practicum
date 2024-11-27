

def main():
    from sys import stdin
    target, *files = [string.strip() for string in stdin]
    found = False

    for file in files:
        with open(file, encoding='UTF-8') as text:
            data = ' '.join(text.read().replace(' ', ' ').lower().split())

            if target.lower() in data:
                print(file)
                found = True

    if not found:
        print('404. Not Found')


if __name__ == "__main__":
    main()
