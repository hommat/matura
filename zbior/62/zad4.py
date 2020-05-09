dec_6_occured = 0
oct_6_occured = 0

with open("liczby2.txt") as l2_file:
  for line in l2_file:
    str_dec_num = line.strip()
    for char in str_dec_num:
      if char == "6":
        dec_6_occured += 1
    
    oct_str_num = str(oct(int(str_dec_num)))
    for char in oct_str_num:
      if char == "6":
        oct_6_occured += 1

print(dec_6_occured)
print(oct_6_occured)