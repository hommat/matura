rows = []

with open("dane.txt") as pixels_file:
  for line in pixels_file:
    row = line.strip().split()
    for index in range(len(row)):
      row[index] = int(row[index])
    rows.append(row)

lightest = -1
darkest = 256

for row in rows:
  for pixel in row:
    lightest = max(lightest, pixel)
    darkest = min(darkest, pixel)

print(lightest)
print(darkest)