import math

def babelkowe(nums):
  n = len(nums)
  for i in range(n):
    for j in range(0, n - i - 1):
      if nums[j] > nums[j + 1]:
        nums[j + 1], nums[j] = nums[j], nums[j + 1]

  return nums

def wybor(nums):
  n = len(nums)
  for i in range(n):
    curr_min = math.inf
    curr_min_j = 0
    for j in range(i, n):
      if nums[j] < curr_min:
        curr_min = nums[j]
        curr_min_j = j
    nums[i], nums[curr_min_j] = nums[curr_min_j], nums[i]

  return nums

def wstawianie_liniowe(nums):
  n = len(nums)
  for i in range(1, n):
    for j in range(i, 0, -1):
      if nums[j] >= nums[j - 1]:
        break;
      else:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
  return nums

def szybkie(tab, lewy, prawy):
  if lewy >= prawy:
    return
  
  i = lewy
  j = prawy
  pivot = tab[math.ceil((lewy + prawy) / 2)]


  while True:    
    while pivot > tab[i]:
      i += 1

    while pivot < tab[j]:
      j -= 1

    if i <= j:
      tab[i], tab[j] = tab[j], tab[i]
      i += 1
      j -= 1
    else:
      break;

  if lewy < j:
    szybkie(tab, lewy, j)
  if prawy > i:
    szybkie(tab, i, prawy)

  return tab