import math

arithmetic_count = 0
max_r = -math.inf

with open("ciagi.txt") as f:
  for i, line in enumerate(f):
    if i % 2 == 0:
      continue

    arr = line.strip().split()
    for j, str_num in enumerate(arr):
      arr[j] = int(str_num)
    
    is_arithmetic = True
    r = arr[1] - arr[0]
    for j in range(1, len(arr)):
      if arr[j] - arr[j-1] != r:
        is_arithmetic = False
        break
    
    if is_arithmetic:
      arithmetic_count += 1
      max_r = max(r, max_r)

print(arithmetic_count)
print(max_r)
    
