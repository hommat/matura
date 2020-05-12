def is_point_in_first_quarter(x, y):
    return x > 0 and y > 0

all_points_in_first_quater_count = 0
with open("wspolrzedne.txt") as data_file:
    for line in data_file:
        nums = line.strip().split()
        for i, num in enumerate(nums):
            nums[i] = int(num)
        
        points = []
        for i in range(0, len(nums), 2):
            points.append([nums[i], nums[i+1]])
        
        all_points_in_first_quater = True
        for point in points:
            if not is_point_in_first_quarter(point[0], point[1]):
                all_points_in_first_quater = False
                break

        if all_points_in_first_quater:
            all_points_in_first_quater_count += 1
print(all_points_in_first_quater_count)