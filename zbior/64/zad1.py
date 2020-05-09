images = [[]]

with open("dane_obrazki.txt") as images_file:
  for line in images_file:
    row = line.strip()
    if row != "":
      images[-1].append(row)
    else:
      images.append([])

reverse_count = 0
max_black_pixels = 0
for image in images:
  black_pixels = 0
  for row in image[0: -1]:
    for pixel in row[0: -1]:
      if pixel == "1":
        black_pixels += 1
  if black_pixels > 200:
    reverse_count += 1
    max_black_pixels = max(max_black_pixels, black_pixels)

print(reverse_count)
print(max_black_pixels)