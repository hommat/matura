import math

images = [[]]

with open("dane_obrazki.txt") as images_file:
  for line in images_file:
    row = line.strip()
    if row != "":
      images[-1].append(row)
    else:
      images.append([])

for i, image in enumerate(images):
  invalid_row_bits = 0
  invalid_rows = []
  for j, row in enumerate(image[0: -1]):
    row_black_pixels = 0
    for pixel in row[0: -1]:
      if pixel == "1":
        row_black_pixels += 1
    if row_black_pixels % 2 != int(row[-1]):
      invalid_row_bits += 1
      invalid_rows.append(j)

  invalid_column_bits = 0
  invalid_columns = []
  for x in range(0, 20):
    column_black_pixels = 0
    for y in range(0, 20):
      pixel = image[y][x]
      if pixel == "1":
        column_black_pixels += 1
    if column_black_pixels % 2 != int(image[20][x]):
      invalid_column_bits += 1
      invalid_columns.append(x)

  if invalid_column_bits == 1 and invalid_row_bits == 1:
    print(i + 1, invalid_rows[0] + 1, invalid_columns[0] + 1)
  elif invalid_column_bits == 0 and invalid_row_bits == 1:
    print(i + 1, invalid_rows[0] + 1, 21)
  elif invalid_column_bits == 1 and invalid_row_bits == 0:
    print(i + 1, 21, invalid_columns[0] + 1)



