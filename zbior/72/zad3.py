max_the_same_end_len = 0
max_the_same_end_len_pairs = []

with open("napisy.txt") as s_file:
  for line in s_file:
    strings = line.strip().split()
    s1 = strings[0]
    s2 = strings[1]
    shorter_len = min(len(s1), len(s2))
    curr_the_same_end_len = 0
    for i in range(1, shorter_len + 1):
      if s1[-i] == s2[-i]:
        curr_the_same_end_len += 1
      else:
        break

    if curr_the_same_end_len > max_the_same_end_len:
      max_the_same_end_len = curr_the_same_end_len
      max_the_same_end_len_pairs = [strings]
    elif curr_the_same_end_len == max_the_same_end_len:
      max_the_same_end_len_pairs.append(strings)


print(max_the_same_end_len)
print(max_the_same_end_len_pairs)