quater_1_count = 0
quater_2_count = 0
quater_3_count = 0
quater_4_count = 0
no_quater_count = 0

def get_circle_points(x, y, r):
    points = [[x, y]]
    points.append([x + r, y])
    points.append([x - r, y])
    points.append([x, y + r])
    points.append([x, y - r])

    return points


def get_point_quater(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0  and y < 0:
        return 3
    elif x > 0  and y < 0:
        return 4
    else:
        return 0

with open("okregi.txt") as circles_file:
    for line in circles_file:
        arr = line.strip().split()
        x = float(arr[0])
        y = float(arr[1])
        r = float(arr[2])
        
        is_in_1 = False
        is_in_2 = False
        is_in_3 = False
        is_in_4 = False
        quater_count = 0

        points = get_circle_points(x, y, r)
        for point in points:
            quater = get_point_quater(point[0], point[1])
            if quater == 0:
                quater_count = 2
                break
            elif quater == 1 and not is_in_1:
                quater_count += 1
                is_in_1 = True
            elif quater == 2 and not is_in_2:
                quater_count += 1
                is_in_2 = True
            elif quater == 3 and not is_in_3:
                quater_count += 1
                is_in_3 = True
            elif quater == 4 and not is_in_4:
                quater_count += 1
                is_in_4 = True
            if quater_count == 2:
                break
        
        if quater_count == 2:
            no_quater_count += 1
        elif is_in_1:
            quater_1_count += 1
        elif is_in_2:
            quater_2_count += 1
        elif is_in_3:
            quater_3_count += 1
        elif is_in_4:
            quater_4_count += 1
            

print(quater_1_count)
print(quater_2_count)
print(quater_3_count)
print(quater_4_count)
print(no_quater_count)