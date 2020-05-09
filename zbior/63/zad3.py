import math

dec_nums = []

with open("ciagi.txt") as c_file:
  for line in c_file:
    c = line.strip()
    dec = int(c, 2)
    dec_nums.append(dec)

def is_prime(n):
  if n == 1:
    return False

  if n == 2:
    return True

  for i in range(2, math.ceil(math.sqrt(n))  + 1):
    if n % i == 0:
      return False

  return True

def generate_primes(m):
  primes = []
  for i in range(1, m + 1):
    if i % 10000 == 0:
      print(str(i) + "/" + str(m))
    if is_prime(i):
      primes.append(i)

  return primes

max_dec = max(dec_nums)
prime_nums = generate_primes(max_dec)
half_prime_nums = 0
max_half_prime = -math.inf
min_half_prime = math.inf

for num in dec_nums:
  for i in range(2, num):
    test_num = num
    if test_num % i == 0:
      if i in prime_nums:
        test_num = int(test_num / i)
        if test_num in prime_nums:
          half_prime_nums += 1
          max_half_prime = max(num, max_half_prime)
          min_half_prime = min(num, min_half_prime)
      break

print(half_prime_nums)
print(max_half_prime)
print(min_half_prime)