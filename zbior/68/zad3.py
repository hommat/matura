def are_anagrams(s1, s2):
  if len(s1) != len(s2):
    return False

  s1_map = { "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0}
  s2_map = { "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0}

  for letter in s1:
    s1_map[letter] += 1

  for letter in s2:
    s2_map[letter] += 1

  for key in s1_map:
    if s1_map[key] != s2_map[key]:
      return False

  return True
 
words = []
with open("dane_napisy.txt") as f:
  for line in f:
    strings = line.strip().split()
    s1 = strings[0]
    s2 = strings[1]

    words.append(s1)
    words.append(s2)

max_anagrams = -1
for i, word1 in enumerate(words):
  curr_anagrams = 1
  for j, word2 in enumerate(words):
    if i == j:
      continue

    if are_anagrams(word1, word2):
      curr_anagrams += 1

  max_anagrams = max(max_anagrams, curr_anagrams)

print(max_anagrams)