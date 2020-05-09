import math

fib_nums = [1, 1]
for n in range(2, 40):
  fib_nums.append(fib_nums[n-1] + fib_nums[n-2])

str_fib_bins = []

for fib_num in fib_nums:
  str_fib_bin = str(bin(fib_num))[2:]
  str_fib_bins.append(str_fib_bin)
  print(str_fib_bin)

print(40*"-")
longest_str_bin_length = len(str_fib_bins[-1])
for str_fib_bin in str_fib_bins:
  for n in range(longest_str_bin_length - len(str_fib_bin)):
    print("0", end="")
  print(str_fib_bin)
  