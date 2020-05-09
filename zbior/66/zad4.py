triangle_count = 0
current_triangle_combo = 0
max_triangle_combo = -1

with open("trojki.txt") as ex_file:
  for line in ex_file:
    nums = line.strip().split()
    n1 = int(nums[0])
    n2 = int(nums[1])
    n3 = int(nums[2])

    if (n1 + n2 > n3) and (n1 + n3 > n2) and (n3 + n2 > n1):
      triangle_count += 1
      current_triangle_combo += 1
      max_triangle_combo = max(max_triangle_combo, current_triangle_combo)
    else:
      current_triangle_combo = 0

print(triangle_count)
print(max_triangle_combo)