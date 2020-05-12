import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)

def is_triangle(l1, l2, l3):
    return l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1

max_c = 0
max_c_points = []

with open("wspolrzedneTR.txt") as data_file:
    for line in data_file:
        nums = line.strip().split()
        for i, num in enumerate(nums):
            nums[i] = int(num)
        
        points = []
        for i in range(0, len(nums), 2):
            points.append([nums[i], nums[i+1]])
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]

        d1 = distance(p1[0], p1[1], p2[0], p2[1])
        d2 = distance(p2[0], p2[1], p3[0], p3[1])
        d3 = distance(p3[0], p3[1], p1[0], p1[1])

        if is_triangle(d1, d2, d3):
            c = round((d1 + d2 + d3) * 100) / 100
            if c > max_c:
                max_c = c
                max_c_points = points

print(max_c)
print(max_c_points)