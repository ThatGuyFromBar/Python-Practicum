

def main():
    with open("secret.txt", encoding='UTF-8') as file:
        text = file.read()
        answer = ""
        for char in text:
            code = ord(char)
            code = code % 256 if code >= 128 else code
            answer += chr(code)

        print(answer)


if __name__ == "__main__":
    main()
