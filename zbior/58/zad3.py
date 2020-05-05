import math

def get_record_days(station, num_system):
  with open("dane_systemy" + str(station) + ".txt") as station_file:
    record_days = []
    current_record = -math.inf
    
    for i, line in enumerate(station_file):
      temp = line.strip().split()[1]
      temp_dec = int(temp, num_system)
      if i == 0 or temp_dec > current_record:
        current_record = temp_dec
        record_days.append(i)

    return record_days

s1_days = get_record_days(1, 2)
s2_days = get_record_days(2, 4)
s3_days = get_record_days(3, 8)

shared_day_count = 0
max_record_day_index = max(max(s1_days), max(s2_days), max(s3_days))
for i in range(max_record_day_index + 1):
  if i in s1_days or i in s2_days or i in s3_days:
    shared_day_count += 1

print(shared_day_count)