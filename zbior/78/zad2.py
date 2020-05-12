def A(nums, d, n):
    w = ""
    for y in nums:
        w += chr((y*d % n))
    return w

with open("podpisy.txt") as signatures_file:
    for line in signatures_file:
        nums = line.strip().split()
        for i, num in enumerate(nums):
            nums[i] = int(num)
        print(A(nums, 3, 200))