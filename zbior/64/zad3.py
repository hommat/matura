import math

images = [[]]

with open("dane_obrazki.txt") as images_file:
  for line in images_file:
    row = line.strip()
    if row != "":
      images[-1].append(row)
    else:
      images.append([])

proper_images_count = 0
repairable_images_count = 0
not_repairable_images_count = 0
max_invalid_bits = -math.inf

for image in images:
  invalid_row_bits = 0
  for row in image[0: -1]:
    row_black_pixels = 0
    for pixel in row[0: -1]:
      if pixel == "1":
        row_black_pixels += 1
    if row_black_pixels % 2 != int(row[-1]):
      invalid_row_bits += 1

  invalid_column_bits = 0
  for x in range(0, 20):
    column_black_pixels = 0
    for y in range(0, 20):
      pixel = image[y][x]
      if pixel == "1":
        column_black_pixels += 1
    if column_black_pixels % 2 != int(image[20][x]):
      invalid_column_bits += 1

  max_invalid_bits = max(max_invalid_bits, invalid_column_bits + invalid_row_bits)
  if invalid_column_bits == 0 and invalid_row_bits == 0:
    proper_images_count += 1
  elif invalid_column_bits <= 1 and invalid_row_bits <= 1:
    repairable_images_count += 1
  else:
    not_repairable_images_count += 1

print(proper_images_count)
print(repairable_images_count)
print(not_repairable_images_count)
print(max_invalid_bits)



