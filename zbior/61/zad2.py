import math

max_cubes = []

with open("ciagi.txt") as f:
  for i, line in enumerate(f):
    if i % 2 == 0:
      continue

    arr = line.strip().split()
    for j, str_num in enumerate(arr):
      arr[j] = int(str_num)
    
    max_arr_num = max(arr)
    max_cube = 0
    j = 1
  
    while True:
      cube = j**3
      if cube > max_arr_num:
        break
      if cube in arr:
        max_cube = cube
      j += 1

    if max_cube > 0:
      max_cubes.append(max_cube)

print(max_cubes)