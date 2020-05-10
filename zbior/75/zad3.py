words_decrypted = []
words_encrypted = []
letters = "abcdefghijklmnopqrstuvwxyz"

with open("probka.txt") as txt_file:
  for line in txt_file:
    words = line.strip().split()
    words_decrypted.append(words[0])
    words_encrypted.append(words[1])

def encrypt(word, a, b):
  encrypted_word = ""
  for letter in word:
    encrypted_letter_index = ((letters.index(letter) * a) + b) % 26
    encrypted_letter = letters[encrypted_letter_index]
    encrypted_word += encrypted_letter
  return encrypted_word

for i in range(0, len(words_decrypted)):
  word_decrypted = words_decrypted[i]
  word_encrypted = words_encrypted[i]
  encrypt_key = ""
  decrypt_key = ""
  for a in range(0, 26):
    for b in range(0, 26):
      if encrypt(word_decrypted, a, b) == word_encrypted:
        encrypt_key = "(" +  str(a) + ", " + str(b) + ")"
      if encrypt(word_encrypted, a, b) == word_decrypted:
        decrypt_key = "(" +  str(a) + ", " + str(b) + ")"