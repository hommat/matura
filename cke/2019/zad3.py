def NWD(a, b):
  while b != 0:
    b, a = a % b, b
  
  return a

nums = []

with open("liczby.txt") as num_file:
  for line in num_file:
    nums.append(int(line.strip()))

max_combo = 0
max_nwd = -1
max_first_num = -1

for start_index in range(len(nums)):
  current_combo = 1
  current_shared_nwd = nums[start_index]
  for index in range(start_index, len(nums) - 1):
    nwd = NWD(current_shared_nwd, nums[index + 1])
    if nwd > 1:
      current_shared_nwd = nwd
      current_combo = current_combo + 1
    else :
      break
  if current_combo > max_combo:
    max_combo = current_combo
    max_nwd = current_shared_nwd
    max_first_num = nums[start_index]
    if max_first_num == 1:
      print(current_shared_nwd)


print(max_combo)
print(max_nwd)
print(max_first_num)
    