

def main():
    old_a = 'abcdefghijklmnopqrstuvwxyz'
    shift = int(input()) % len(old_a)
    new_a = old_a[shift:] + old_a[:shift]

    alphabet = {key: value for key, value in zip(old_a, new_a)}
    answer = ''
    with open("public.txt", encoding='UTF-8') as file:
        text = file.read()
        for char in text:
            new = alphabet[char.lower()] if char.lower() in alphabet else char
            answer += new.upper() if char.isupper() else new
    with open("private.txt", 'w', encoding='UTF-8') as file:
        file.write(answer)


if __name__ == "__main__":
    main()
