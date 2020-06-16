rows = []

with open("dane.txt") as pixels_file:
  for line in pixels_file:
    row = line.strip().split()
    for index in range(len(row)):
      row[index] = int(row[index])
    rows.append(row)

rows_to_delete = 0

for row in rows:
  delete_row = False
  for index in range(0, int(len(rows[0]) / 2)):
    if row[index] != row[-index - 1]:
      delete_row = True
      break
  if delete_row:
    rows_to_delete += 1

print(rows_to_delete)