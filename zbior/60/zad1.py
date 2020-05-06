less_than_1000 = []
with open("liczby.txt") as num_file:
  for line in num_file:
    n = int(line.strip())
    if n < 1000:
      less_than_1000.append(n)

print(len(less_than_1000))
print(less_than_1000[-2], less_than_1000[-1])