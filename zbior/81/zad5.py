import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)

def is_triangle(l1, l2, l3):
    return l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1

with open("wspolrzedneTR.txt") as data_file:
    for line in data_file:
        nums = line.strip().split()
        for i, num in enumerate(nums):
            nums[i] = int(num)
        
        points = []
        for i in range(0, len(nums), 2):
            points.append([nums[i], nums[i+1]])
        points.append([0, 0])

        A = points[0]
        B = points[1]
        C = points[2]
        D = points[3]

        D[0] = A[0] + (C[0] - B[0])
        D[1] = A[1] + (C[1] - B[1])
        
        if D[0] == D[1]:
            print(A, B, C, D)
