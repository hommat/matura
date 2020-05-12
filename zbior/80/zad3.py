lengths = []
with open("dane_trojkaty.txt") as data_file:
    for line in data_file:
        num = int(line.strip())
        lengths.append(num)

def can_be_triangle(l1, l2, l3):
    return l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1


lengths.sort()
count = 0

for x in range(0, len(lengths) - 2):
    for y in range(x + 1, len(lengths) - 1):
        for z in range(y + 1, len(lengths)):
            l1 = lengths[x]
            l2 = lengths[y]
            l3 = lengths[z]
            if can_be_triangle(l1, l2, l3):
                count += 1
            else:
                break

print(count)