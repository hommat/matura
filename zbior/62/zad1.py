import math

min_dec = math.inf
max_dec = -math.inf
min_oct = 0
max_oct = 0

with open("liczby1.txt") as num_file:
  for line in num_file:
    oct_num = line.strip()
    dec_num = int(oct_num, 8)

    if dec_num > max_dec:
      max_dec = dec_num
      max_oct = oct_num
    
    if dec_num < min_dec:
      min_dec = dec_num
      min_oct = oct_num

print("min: " + min_oct)
print("max: " + max_oct)