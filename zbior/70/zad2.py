import math

def distance(x1, y1, x2, y2):
  x = abs(x2 - x1)
  y = abs(y2 - y1)

  return math.sqrt(y**2 + x **2)
  
def f(x):
  return (x**4)/500 - (x**2)/200 - 3/250

def g(x):
  return -(x**3)/30 + x/20 +1/6

o = 19 + 61/125 + 32 + 2/3 + 8 + 8
x_per_iteration = 0.008

points_top = []
x = 2

while x <= 10:
  y = f(x)
  points_top.append(x)
  points_top.append(y)
  x += x_per_iteration

for i in range(0, int(len(points_top)/2) - 1):
  dist = distance(points_top[i * 2], points_top[i *2 + 1], points_top[i *2 + 2], points_top[i *2 + 3])
  o += dist

points_bottom = []
x = 2

while x <= 10:
  y = g(x)
  points_bottom.append(x)
  points_bottom.append(y)
  x += x_per_iteration

for i in range(0, int(len(points_bottom)/2) - 1):
  dist = distance(points_bottom[i * 2], points_bottom[i *2 + 1], points_bottom[i *2 + 2], points_bottom[i *2 + 3])
  o += dist

print(math.ceil(o))
