times_3_bigger_count = 0
with open("napisy.txt") as s_file:
  for line in s_file:
    strings = line.strip().split()
    s1 = strings[0]
    s2 = strings[1]
    if(len(s1) >= len(s2)):
      continue

    can_be = True
    for i in range(0, len(s1)):
      if s1[i] != s2[i]:
        can_be = False
        break

    if not can_be:
      continue

    print(s1, s2)
    for i in range(len(s1), len(s2)):
      print(s2[i], end="")
    print()
