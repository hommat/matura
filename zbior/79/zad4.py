import math

circles = []
with open("okregi.txt") as circles_file:
    j = 0
    for line in circles_file:
        circle = line.strip().split()
        for i, num in enumerate(circle):
            circle[i] = float(num)
        circles.append(circle)
        j += 1
        if j == 1000:
            break

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)

def has_point(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    r_sum = r1 + r2

    if d > r_sum or d + min(r1, r2) < max(r1, r2):
        return False
    else:
        return True
    
max_combo = 0
current_combo = 1
for i in range(0, len(circles) - 1):
    x = circles[i][0]
    y = circles[i][1]
    r = circles[i][2]

    next_x = circles[i + 1][0]
    next_y = circles[i + 1][1]
    next_r = circles[i + 1][2]

    if has_point(x, y, r, next_x, next_y, next_r):
        current_combo += 1
    else:
        print(current_combo)
        max_combo = max(current_combo, max_combo)
        current_combo = 1

print(current_combo)
print(max_combo)

