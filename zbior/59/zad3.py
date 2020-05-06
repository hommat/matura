import math

def mult_nums_in_n(n):
  str_n = str(n)
  s = 1
  for str_num in str_n:
    s = s * int(str_num)
  
  return s

def calculate_power(n):
  curr_power = 1
  curr_n = mult_nums_in_n(n)
  while curr_n >= 10:
    curr_power += 1
    curr_n = mult_nums_in_n(curr_n)

  return curr_power

max_pow_1 = -math.inf
min_pow_1 = math.inf
pow_dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7:0, 8:0}

with open("liczby.txt") as num_file:
  for line in num_file:
    num = int(line.strip())
    num_pow = calculate_power(num)
    pow_dic[num_pow] = pow_dic[num_pow] + 1
    if num_pow == 1:
      max_pow_1 = max(num, max_pow_1)
      min_pow_1 = min(num, min_pow_1)

print(min_pow_1, max_pow_1)
print(pow_dic)