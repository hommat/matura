fn_arr = []
with open("funkcja.txt") as fn_file:
  for line in fn_file:
    fn = line.strip().split()
    for i, num in enumerate(fn):
      fn[i] = float(num)
    fn_arr.append(fn)

def f(x):
  if x >= 0 and x < 1:
    return fn_arr[0][0] + fn_arr[0][1] * x + fn_arr[0][2] * x * x + fn_arr[0][3] * x * x * x 
  elif x >= 1 and x < 2:
    return fn_arr[1][0] + fn_arr[1][1] * x + fn_arr[1][2] * x * x + fn_arr[1][3] * x * x * x 
  elif x >= 2 and x < 3:
    return fn_arr[2][0] + fn_arr[2][1] * x + fn_arr[2][2] * x * x + fn_arr[2][3] * x * x * x 
  elif x >= 3 and x < 4:
    return fn_arr[3][0] + fn_arr[3][1] * x + fn_arr[3][2] * x * x + fn_arr[3][3] * x * x * x 
  elif x >= 4 and x < 5:
    return fn_arr[4][0] + fn_arr[4][1] * x + fn_arr[4][2] * x * x + fn_arr[4][3] * x * x * x  

print(f(1.5))