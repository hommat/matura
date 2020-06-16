rows = []

with open("dane.txt") as pixels_file:
  for line in pixels_file:
    row = line.strip().split()
    for index in range(len(row)):
      row[index] = int(row[index])
    rows.append(row)

longest_line = 0

for x in range(len(rows[0])):
  current_combo = 0
  current_value = -1
  for y in range(len(rows)):
    current_pixel = rows[y][x]
    if current_pixel == current_value:
      current_combo += 1
    else:
      longest_line = max(current_combo, longest_line)
      current_combo = 1
      current_value = current_pixel

print(longest_line)
