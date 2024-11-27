
def main():
    text = ""
    with open(input(), encoding='UTF-8') as base_text:
        for line in base_text:
            text += line
    while "  " in text or "\n\n" in text or "\t" in text or "\n " in text or " \n" in text:
        text = text.replace("  ", " ")
        text = text.replace("\n\n", "\n")
        text = text.replace("\t", "")
        text = text.replace("\n ", "\n")
        text = text.replace(" \n", "\n")
    if text[0] == " ":
        text = text.replace(" ", "", 1)
    if text[-1] == "\n":
        text = text[:-1]
    with open(input(), 'w', encoding='UTF-8') as finished_text:
        print(text, file=finished_text)


if __name__ == "__main__":
    main()
