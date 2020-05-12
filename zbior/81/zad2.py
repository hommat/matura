all_points_in_one_line_count = 0
with open("wspolrzedne.txt") as data_file:
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

        
        if p1[0] - p2[0] == 0:
            if p2[0] - p3[0] == 0:
                all_points_in_one_line_count += 1
        elif p2[0] - p3[0] != 0:
            a_1 = (p1[1] - p2[1])/(p1[0] - p2[0])
            b_1 = p1[1] - a_1*p1[0]
            
            a_2 = (p2[1] - p3[1])/(p2[0] - p3[0])
            b_2 = p2[1] - a_2*p2[0]
            max_error = 0.0000001
            
            if abs(abs(a_1) - abs(a_2)) <= max_error and abs(abs(b_1) - abs(b_2)) <= max_error:
                all_points_in_one_line_count += 1

print(all_points_in_one_line_count)