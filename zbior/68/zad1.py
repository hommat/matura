count = 0

def check(s1, s2):
  if len(s1) != len(s2):
    return False

  s1_letter = s1[0]
  s2_letter = s2[0]

  for letter in s1:
    if letter != s1_letter:
      return False

  for letter in s2:
    if letter != s2_letter:
      return False
  
  return s1_letter == s2_letter

with open("dane_napisy.txt") as f:
  for line in f:
    strings = line.strip().split()
    s1 = strings[0]
    s2 = strings[1]

    if check(s1, s2):
      count += 1

print(count)

    