with open("trojki.txt") as ex_file:
  for line in ex_file:
    nums = line.strip().split()
    n1 = int(nums[0])
    n2 = int(nums[1])
    n3 = int(nums[2])

    if (n1 ** 2 + n2 ** 2 == n3 ** 2) or (n1 ** 2 + n3 ** 2 == n2 ** 2) or (n3 ** 2 + n2 ** 2 == n1 ** 2):
      print(nums)