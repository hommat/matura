with open("bledne.txt") as f:
  for i, line in enumerate(f):
    if i % 2 == 0:
      continue

    arr = line.strip().split()
    for j, str_num in enumerate(arr):
      arr[j] = int(str_num)

    diff_dict = {}

    for j in range(1, len(arr)):
      diff = arr[j] - arr[j-1]
      if diff in diff_dict:
        if diff_dict[diff] == 2:
          correct_diff = diff
          break
        diff_dict[diff] += 1
      else:
        diff_dict[diff] = 1

    correct_diff = 0
    for key in diff_dict:
      if diff_dict[key] == 2:
        correct_diff = key

    for j in range(0, len(arr) - 1):
      if arr[j] + correct_diff != arr[j + 1]:
        print(arr[j+1])
        break 
    
  