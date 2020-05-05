import math

temps=[]
with open("dane_systemy1.txt") as station_file:
  for i, line in enumerate(station_file):
    temp = line.strip().split()[1]
    temp_dec = int(temp, 2)
    temps.append(temp_dec)

max_jump = -math.inf
for i in range(0, len(temps) - 1):
  for j in range(i + 1, len(temps)):
    t_i = temps[i]
    t_j = temps[j]
    r_ij = (t_i - t_j) * (t_i - t_j)
    diff = abs(i - j)
    jump = math.ceil(r_ij / diff)
    max_jump = max(jump, max_jump)
    
print(max_jump)