words = []
letters = "abcdefghijklmnopqrstuvwxyz"

with open("tekst.txt") as txt_file:
  for line in txt_file:
    words = line.strip().split()

def encrypt(word, a, b):
  encrypted_word = ""
  for letter in word:
    encrypted_letter_index = ((letters.index(letter) * a) + b) % 26
    encrypted_letter = letters[encrypted_letter_index]
    encrypted_word += encrypted_letter
  return encrypted_word

for word in words:
  if len(word) >= 10:
    print(encrypt(word, 5, 2))