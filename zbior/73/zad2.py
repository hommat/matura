letters_count = 0
letters_map = {}
with open("tekst.txt") as words_file:
  for line in words_file:
    words = line.strip().split()

for word in words:
  letters_count += len(word)
  for letter in word:
    if letter not in letters_map:
      letters_map[letter] = 1
    else:
      letters_map[letter] += 1

sorted_keys = []
for key in letters_map:
  sorted_keys.append(key)
sorted_keys.sort()

for key in sorted_keys:
  value = letters_map[key]
  percent = round((value * 10000)/letters_count)/100
  print(key+":", value, "(" + str(percent) + "%)" )
    