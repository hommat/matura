l1 = []
l2 = []

the_same_count = 0
l1_bigger_count = 0

with open("liczby1.txt") as l1_file:
  for line in l1_file:
    num = int(line.strip(), 8)
    l1.append(num)

with open("liczby2.txt") as l2_file:
  for line in l2_file:
    num = int(line.strip())
    l2.append(num)

for i in range(0, len(l1)):
  if l1[i] == l2[i]:
    the_same_count += 1
  elif l1[i] > l2[i]:
    l1_bigger_count += 1

print(the_same_count)
print(l1_bigger_count)