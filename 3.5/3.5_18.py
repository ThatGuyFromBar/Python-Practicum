

def main():
    with open(input(), 'rb') as file:
        text = file.read()
    size = len(text)

    form = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    n = 0

    while size > 1024 and n < len(form):
        n += 1
        if size % 1024 > 0:
            size = (size // 1024) + 1
        else:
            size = size // 1024

    print(f'{size}{form[n]}')


if __name__ == "__main__":
    main()
