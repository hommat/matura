import math

def is_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True

  for i in range(2, math.ceil(math.sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True

with open("trojki.txt") as ex_file:
  for line in ex_file:
    nums = line.strip().split()
    n1 = int(nums[0])
    n2 = int(nums[1])
    n3 = int(nums[2])

    if n3 == n1 * n2 and is_prime(n1) and is_prime(n2):
      print(nums)