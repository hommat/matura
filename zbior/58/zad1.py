import math

def get_min_temp(station, num_system):
  with open("dane_systemy" + str(station) + ".txt") as station_file:
    min_temp_dec = math.inf
    for line in station_file:
      temp = line.strip().split()[1]
      temp_dec = int(temp, num_system)
      min_temp_dec = min(temp_dec, min_temp_dec)

    return min_temp_dec

s1_min_temp = get_min_temp(1, 2)
print(bin(s1_min_temp))

s2_min_temp = get_min_temp(2, 4)
print(bin(s2_min_temp))

s3_min_temp = get_min_temp(3, 8)
print(bin(s3_min_temp))
