a = 200
b = 200
r = 200

def is_on_circle(x, y):
  return (x - a)**2 + (y - b)**2 == r**2

def is_in_circle(x, y):
  return (x - a)**2 + (y - b)**2 < r**2

in_circle_count = 0

with open("punkty.txt") as points_file:
  for line in points_file:
    points = line.strip().split()
    x = int(points[0])
    y = int(points[1])
    if is_on_circle(x, y):
      on_circle_count += 1
    elif is_in_circle(x, y):
      in_circle_count += 1

print("on circle")
print(on_circle_count)
print("in circle")
print(in_circle_count)