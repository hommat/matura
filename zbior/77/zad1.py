import math

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(word, key):
  encrypted_word = ""
  key_len = len(key)
  k = 0
 
  for char in word:
    if char == " " or char == "," or char == ".":
      encrypted_word += char
    else:
      char_index = letters.index(char)
      key_index = letters.index(key[k % key_len])
      encrypted_char_index = (char_index + key_index) % (len(letters))
      encrypted_char = letters[encrypted_char_index]
      encrypted_word += encrypted_char
      k += 1

  key_repetition = math.ceil(k / key_len)
  return encrypted_word, key_repetition

with open("dokad.txt") as txt_file:
  for line in txt_file:
    word = line.strip()

encrypted_word, key_repetition = encrypt(word, "LUBIMYCZYTAC")
print(encrypted_word)
print(key_repetition)