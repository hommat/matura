import math

with open("ciagi.txt") as c_file:
  for line in c_file:
    c = line.strip()
    c_len = len(c)
    c_half_len = int(c_len / 2)
    if c_len % 2 != 0:
      continue

    is_double = True
    for i in range(0, c_half_len):
      if c[i] != c[i + c_half_len]:
        is_double = False
        break
    
    if is_double:
      print(c)
