images = [[]]

with open("dane_obrazki.txt") as images_file:
  for line in images_file:
    row = line.strip()
    if row != "":
      images[-1].append(row)
    else:
      images.append([])

recurrent_images_count = 0
first_recurrent_image = []

for image in images:
  is_recurrent = True
  for x in range(0, 10):
    for y in range(0, 10):
      if image[x][y] != image[x + 10][y] or image[x][y] != image[x][y + 10] or image[x][y] != image[x + 10][y + 10]:
        is_recurrent = False
        break
    if not is_recurrent:
      break
  
  if is_recurrent:
    recurrent_images_count += 1
    if recurrent_images_count == 1:
      for row in image[0: -1]:
        first_recurrent_image.append([])
        for pixel in row[0:-1]:
          first_recurrent_image[-1].append(pixel)

print(recurrent_images_count)
for row in first_recurrent_image:
  print(row)
