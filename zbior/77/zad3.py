with open("szyfr.txt") as txt_file:
  lines = []
  for line in txt_file:
    lines.append(line.strip())
  word = lines[0]
  key_len = len(lines[1])

char_map = {
  "A": 0,
  "B": 0,
  "C": 0,
  "D": 0,
  "E": 0,
  "F": 0,
  "G": 0,
  "H": 0,
  "I": 0,
  "J": 0,
  "K": 0,
  "L": 0,
  "M": 0,
  "N": 0,
  "O": 0,
  "P": 0,
  "Q": 0,
  "R": 0,
  "S": 0,
  "T": 0,
  "U": 0,
  "V": 0,
  "W": 0,
  "X": 0,
  "Y": 0,
  "Z": 0,
}

letters_in_word = 0

for char in word:
  if char in char_map.keys():
    char_map[char] += 1
    letters_in_word += 1

print(char_map)

k_top = 0
for key in char_map.keys():
  k_top += char_map[key] * (char_map[key] - 1)

k_bottom = letters_in_word * (letters_in_word - 1)
k = k_top/k_bottom
d = 0.0285 / (k - 0.0385)
print(key_len)
print(d)