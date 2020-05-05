def get_wrong_days(station, num_system):
  with open("dane_systemy" + str(station) + ".txt") as station_file:
    wrong_days=[]
    for i, line in enumerate(station_file):
      time = line.strip().split()[0]
      required_time = 12 + 24 * i
      time_dec = int(time, num_system)
      if time_dec != required_time:
        wrong_days.append(i)
      
    return wrong_days

s1_days = get_wrong_days(1, 2)
s2_days = get_wrong_days(2, 4)
s3_days = get_wrong_days(3, 8)

shared_day_count = 0
for day in s1_days:
  if day in s2_days and day in s3_days:
    shared_day_count += 1

print(shared_day_count)