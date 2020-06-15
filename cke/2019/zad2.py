def s(n):
  num = 1

  for x in range(1, n + 1):
    num = num * x

  return num

with open("liczby.txt") as num_file:
  for line in num_file:
    digits = line.strip()
    digits_sum = 0
    for digit in digits:
      num = s(int(digit))
      digits_sum = digits_sum + num
    if(int(digits) == digits_sum):
      print(digits)
    