import math

with open("liczby.txt") as num_file:
  for line in num_file:
    d_arr = [1]
    n = int(line.strip())
    too_much = False
    for d in range(2, math.ceil(n/2) + 1):
      if n % d == 0:
        d_arr.append(d)
        if len(d_arr) > 17:
          too_much = True
          break 

    d_arr.append(n)
    if len(d_arr) == 18:
      print(str(n) + " - " + str(d_arr))
