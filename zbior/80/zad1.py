lengths = []
with open("dane_trojkaty.txt") as data_file:
    for line in data_file:
        num = int(line.strip())
        lengths.append(num)

for i in range(0, len(lengths) - 2):
    sorted_lengths = sorted([lengths[i], lengths[i + 1], lengths[i + 2]])
    if sorted_lengths[0] ** 2 + sorted_lengths[1] ** 2 == sorted_lengths[2] ** 2:
        print(lengths[i], lengths[i + 1], lengths[i + 2])