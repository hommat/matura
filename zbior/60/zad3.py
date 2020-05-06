import math

def get_div_arr(n):
  divs = []
  for d in range(2, math.ceil(n/2) + 1):
    if n % d == 0:
      divs.append(d)

  return divs

max_num = -math.inf
d_dict = {}

with open("liczby.txt") as num_file:
  for line in num_file:
    n = int(line.strip())
    dividers = get_div_arr(n)
    d_dict[n] = dividers

for i, dict_num in enumerate(d_dict):
  if dict_num <= max_num:
    continue
  is_prime = True
  dict_dividers = d_dict[dict_num]
  for j, other_dict_num in enumerate(d_dict):
    if j <= i:
      continue
    other_dict_dividers = d_dict[other_dict_num]
    for dict_divider in dict_dividers:
      if dict_divider in other_dict_dividers:
        is_prime = False
        break
    if is_prime == False:
      break
  if is_prime:
    max_num = max(dict_num, max_num)

print(max_num)


