def shortcut(message):
    S = []
    for char in "ALGORYTM":
        S.append(ord(char))

    while len(message) % 8 != 0:
        message += "."

    print(len(message))

    for i, char in enumerate(message):
        S[i % 8] = (S[i % 8] + ord(char)) % 128

    print(S)

    wynik = ""
    for i in range(0, 8):
        wynik += chr(65 + S[i] % 26)

    return wynik

with open("wiadomosci.txt") as mess_file:
    first_message = ""
    for line in mess_file:
        first_message = line.strip()
        break

print(shortcut(first_message))