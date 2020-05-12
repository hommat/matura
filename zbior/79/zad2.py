circles = []
with open("okregi.txt") as circles_file:
    for line in circles_file:
        circle = line.strip().split()
        for i, num in enumerate(circle):
            circle[i] = float(num)
        circles.append(circle)
        
total_pair_count = 0
checked_r = []
for i, circle in enumerate(circles):
    x = circle[0]
    y = circle[1]
    r = circle[2]

    if r in checked_r:
        continue
    checked_r.append(r)
    pair_count = 0
    has_opposite_circle = False

    for j, circle_2 in enumerate(circles):
        x_2 = circle_2[0]
        y_2 = circle_2[1]
        r_2 = circle_2[2]

        if i == j:
            continue
        if r != r_2 or abs(x) != abs(x_2) or abs(y) != abs(y_2):
            continue
        

        if x == x_2 or y == y_2:
            if pair_count == 0 and has_opposite_circle:
                pair_count += 2
            else:
                pair_count += 1
        else:
            if pair_count == 0:
                has_opposite_circle = True
            else:
                pair_count += 1 
    
    if pair_count == 3:
        pair_count += 1
    total_pair_count += pair_count

print(total_pair_count)
