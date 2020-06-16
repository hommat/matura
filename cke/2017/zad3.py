rows = []

with open("dane.txt") as pixels_file:
  for line in pixels_file:
    row = line.strip().split()
    for index in range(len(row)):
      row[index] = int(row[index])
    rows.append(row)

contrast_count = 0

for y in range(len(rows)):
  for x in range(len(rows[y])):
    current_pixel = rows[y][x]

    # on right
    if x + 1 < len(rows[y]):
      right_pixel = rows[y][x + 1]
      if abs(current_pixel - right_pixel) > 128:
        contrast_count += 1
        continue

    # on left
    if x - 1 >= 0:
      left_pixel = rows[y][x - 1]
      if abs(current_pixel - left_pixel) > 128:
        contrast_count += 1
        continue

    # on bottom
    if y + 1 < len(rows):
      bottom_pixel = rows[y + 1][x]
      if abs(current_pixel - bottom_pixel) > 128:
        contrast_count += 1
        continue
    
    # on top
    if y - 1 >= 0:
      top_pixel = rows[y - 1][x]
      if abs(current_pixel - top_pixel) > 128:
        contrast_count += 1
        continue