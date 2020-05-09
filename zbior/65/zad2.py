import math

def get_prime_dividers(num):
  dividers = []
  divider = 2
  while (num > 1):
    if num % divider == 0:
      dividers.append(divider)
    while (num % divider == 0):
      num = num / divider
    divider += 1

  return dividers

fractions_that_can_be_shorter_count = 0

with open("dane_ulamki.txt") as ex_file:
  for line in ex_file:
    fraction = line.strip().split() #n/d
    n = int(fraction[0])
    d = int(fraction[1])
    n_dividers = get_prime_dividers(n)
    d_dividers = get_prime_dividers(d)
    can_be_shorter = False

    for n_divider in n_dividers:
      if n_divider in d_dividers:
        can_be_shorter = True
        break

    if can_be_shorter:
      fractions_that_can_be_shorter_count += 1

print(fractions_that_can_be_shorter_count)