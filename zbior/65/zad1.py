import math

min_fraction_dec = math.inf
min_n = math.inf
min_d = math.inf

with open("dane_ulamki.txt") as ex_file:
  for line in ex_file:
    fraction = line.strip().split() #n/d
    n = int(fraction[0])
    d = int(fraction[1])
    dec = n/d
    if dec < min_fraction_dec:
      min_fraction_dec = dec
      min_n = n
      min_d = d
    elif dec == min_fraction_dec and d < min_d:
      min_n = n
      min_d = d

print(min_n, "/", min_d)
    