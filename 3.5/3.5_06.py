
def main():
    alphabet = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
    }
    text = ""
    trans_text = ""
    with open("cyrillic.txt", encoding="UTF-8") as base_text:
        for line in base_text:
            text += line

    for char in text:
        if char.upper() in alphabet:
            trans_text += alphabet[char.upper()].lower().capitalize() if char == char.upper() \
                else alphabet[char.upper()].lower()
        else:
            trans_text += char
    with open("transliteration.txt", "w", encoding="UTF-8") as finished_text:
        print(trans_text, file=finished_text)


if __name__ == "__main__":
    main()
