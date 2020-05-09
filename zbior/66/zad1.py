with open("trojki.txt") as ex_file:
  for line in ex_file:
    nums = line.strip().split()
    num1_sum = 0
    num2_sum = 0
    for num in nums[0]:
      num1_sum += int(num)

    for num in nums[1]:
      num2_sum += int(num)

    if(num1_sum + num2_sum == int(nums[2])):
      print(nums)