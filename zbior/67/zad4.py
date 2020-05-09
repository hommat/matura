import math

fib_nums = [1, 1]
for n in range(2, 40):
  fib_nums.append(fib_nums[n-1] + fib_nums[n-2])

for fib_num in fib_nums:
  str_fib_bin = str(bin(fib_num))[2:]
  ones_count = 0
  for char in str_fib_bin:
    if char == "1":
      ones_count += 1
  if ones_count == 6:
    print(str_fib_bin)

  
  