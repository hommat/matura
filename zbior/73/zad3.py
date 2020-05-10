longest_subword_len = 0
words_with_longest_subword = []

with open("tekst.txt") as words_file:
  for line in words_file:
    words = line.strip().split()

for word in words:
  curr_subword_len = 0
  curr_longest_subword_len = 0
  for letter in word:
    if letter not in ["A", "E", "I", "O", "U", "Y"]:
      curr_subword_len += 1
      curr_longest_subword_len = max(curr_longest_subword_len, curr_subword_len)
    else:
      curr_subword_len = 0

  if curr_longest_subword_len > longest_subword_len:
    longest_subword_len = curr_longest_subword_len
    words_with_longest_subword = [word]
  elif curr_longest_subword_len == longest_subword_len:
    words_with_longest_subword.append(word)
    

print(longest_subword_len)
print(len(words_with_longest_subword))
print(words_with_longest_subword[0])
    