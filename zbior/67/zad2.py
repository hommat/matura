import math

fib_nums = [1, 1]
for n in range(2, 40):
  fib_nums.append(fib_nums[n-1] + fib_nums[n-2])

def is_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True

  for i in range(2, math.ceil(math.sqrt(n))+1):
    if n % i == 0:
      return False

  return True 

for fib_num in fib_nums:
  if is_prime(fib_num):
    print(fib_num)