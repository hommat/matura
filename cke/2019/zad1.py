power_3_count = 0

with open("liczby.txt") as num_file:
  for line in num_file:
    num = int(line.strip())
    while num > 1:
      num = num / 3

    if num == 1:
      power_3_count += 1

print(power_3_count)
    