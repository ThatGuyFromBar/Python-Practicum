def main():
    s = input()
    translit = {'А': 'a', 'Б': 'b', 'В': 'v', 'Г': 'g', 'Д': 'd', 'Е': 'e', 'Ё': 'e', 'Ж': 'zh', 'З': 'z', 'И': 'i',
                'Й': 'i', 'К': 'k', 'Л': 'l', 'М': 'm', 'Н': 'n', 'О': 'o', 'П': 'p', 'Р': 'r', 'С': 's', 'Т': 't',
                'У': 'u', 'Ф': 'f', 'Х': 'kh', 'Ц': 'tc', 'Ч': 'ch', 'Ш': 'sh', 'Щ': 'shch', 'Ы': 'y', 'Э': 'e',
                'Ю': 'iu', 'Я': 'ia'}
    s = s.replace("ъ", "").replace("Ъ", "").replace("ь", "").replace("Ь", "")
    snew = ""
    for i in range(len(s)):
        if translit.__contains__(s[i].capitalize()):
            if not (s[i].islower()):
                snew += translit[s[i].capitalize()][0].capitalize() + translit[s[i].capitalize()][1:]
            else:
                snew += translit[s[i].capitalize()]
        else:
            snew += s[i]
    print(snew)


if __name__ == "__main__":
    main()
