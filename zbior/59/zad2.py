def invert_n(n):
  str_n = str(n)
  inverted_str_n = ""
  for i in range(len(str_n), 0, -1):
    inverted_str_n += str_n[i-1]
    
  return int(inverted_str_n)

def sum_n_and_inverted_n(n):
  return n + invert_n(n)

how_much = 0
with open("liczby.txt") as num_file:
  for line in num_file:
    n = int(line.strip())
    s = sum_n_and_inverted_n(n)
    inverted_s = invert_n(s)
    if s == inverted_s:
      how_much += 1

print(how_much)
