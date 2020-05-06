def has_3_diff_primes(n):
  if n % 2 == 0:
    return False

  diff_primes = 0
  k = 3

  while n > 1:
    if n % k == 0:
      diff_primes += 1
      if diff_primes > 3:
        return False
    while n % k == 0:
      n = n / k
    k += 1
  
  return diff_primes == 3

with open("liczby.txt") as my_file:
  how_much = 0
  for line in my_file:
    n = int(line.strip())
    if has_3_diff_primes(n):
      how_much += 1

  print(how_much)
    