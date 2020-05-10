the_same_letters_after_count = 0
words = []
with open("tekst.txt") as words_file:
  for line in words_file:
    words = line.strip().split()

for word in words:
  for i in range(0, len(word) - 1):
    if word[i] == word[i+1]:
      the_same_letters_after_count += 1
      break

print(the_same_letters_after_count)
    