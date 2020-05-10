def replace_string_letters(string, index1, index2):
  helper_arr = []
  for char in string:
    helper_arr.append(char)

  temp = helper_arr[index2]
  helper_arr[index2] = helper_arr[index1]
  helper_arr[index1] = temp
  
  replaced_string = ""
  for char in helper_arr:
    replaced_string += char

  return replaced_string

def decrypt(word, key):
  decrypted_word = word
  n = len(key)

  for i in range(len(word) - 1, -1, -1):
    decrypted_word = replace_string_letters(decrypted_word, i, key[i % n] - 1)

  return decrypted_word

with open("szyfr3.txt") as txt_file:
  for line in txt_file:
    word = line.strip()

print(decrypt(word, [6, 2, 4, 1, 5, 3]))