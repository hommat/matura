def wolny(a, b):
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  
  return a

def szybki(a, b):
  while b != 0:
    temp = b
    b = a % b
    a = temp

  return a