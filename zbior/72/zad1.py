times_3_bigger_count = 0
with open("napisy.txt") as s_file:
  for line in s_file:
    strings = line.strip().split()
    s1 = strings[0]
    s2 = strings[1]
    longer_len = max(len(s1), len(s2))
    shorter_len = min(len(s1), len(s2))
    if longer_len / shorter_len >= 3:
      if times_3_bigger_count == 0:
        print(strings)
      times_3_bigger_count += 1

print(times_3_bigger_count)