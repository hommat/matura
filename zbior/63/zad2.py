not_double_ones = 0

with open("ciagi.txt") as c_file:
  for line in c_file:
    c = line.strip()
    has_double_ones = False
    for i in range(0, len(c) - 1):
      if c[i] != "1":
        continue
      if c[i] == c[i+1]:
        has_double_ones = True
        break

    if not has_double_ones:
      not_double_ones += 1

print(not_double_ones)

