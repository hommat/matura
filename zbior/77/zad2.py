import math

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(word, key):
  decrypted_word = ""
  key_len = len(key)
  k = 0
 
  for char in word:
    if char == " " or char == "," or char == ".":
      decrypted_word += char
    else:
      char_index = letters.index(char)
      key_index = letters.index(key[k % key_len])
      decrypted_char_index = abs((char_index - key_index) % (len(letters)))
      decrypted_char = letters[decrypted_char_index]
      decrypted_word += decrypted_char
      k += 1

  return decrypted_word

with open("szyfr.txt") as txt_file:
  lines = []
  for line in txt_file:
    lines.append(line.strip())
  word = lines[0]
  key = lines[1]

decrypted_word = decrypt(word, key)
print(decrypted_word)
