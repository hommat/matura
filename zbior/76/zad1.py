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

def encrypt(word, key):
  encrypted_word = word
  n = len(key)

  for i in range(0, len(word)):
    encrypted_word = replace_string_letters(encrypted_word, i, key[i % n] - 1)

  return encrypted_word

words = []
key = []
with open("szyfr1.txt") as txt_file:
  lines = []
  for i, line in enumerate(txt_file):
    lines.append(line.strip())
  for word in lines[:-1]:
    words.append(word)
  key_line_str_nums = lines[-1].split()
  for str_num in key_line_str_nums:
    key.append(int(str_num))

for word in words:
  encrypted_word = encrypt(word, key)
  print(encrypted_word)