text = input()
print({symb: text.lower().count(symb) for symb in set(text.lower()) if symb.isalpha()})
