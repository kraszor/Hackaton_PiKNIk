def palindrom(text):
    return True if text.lower().replace(" ", "") == text[::-1].lower().replace(" ", "") else False


print(palindrom("maciej"))
print(palindrom("ala"))
print(palindrom("Ala"))
print(palindrom("Może jutro ta dama da tortu jeżom"))
print(palindrom("Kobyła ma mały bok"))