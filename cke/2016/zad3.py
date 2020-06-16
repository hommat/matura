import math

a = 200
b = 200
r = 200

def is_in_circle(x, y):
  return (x - a)**2 + (y - b)**2 <= r**2

def get_points(points_count):
  points = []
  with open("punkty.txt") as points_file:
    for line in points_file:
      line_points = line.strip().split()
      x = int(line_points[0])
      y = int(line_points[1])
      points.append([x, y])
      if(len(points) == points_count):
        return points

def calculate_points_in_circle(points):
  points_in_circle = 0
  for point in points:
    if is_in_circle(point[0], point[1]):
      points_in_circle += 1
  return points_in_circle

def calculate_pi(points_count):
  points = get_points(points_count)
  points_in_circle = calculate_points_in_circle(points)
  pi = (points_in_circle*(r*2)**2)/(points_count*r**2)

  return pi


with open("ouput.txt", "a") as output_file:
  for i in range(1, 1701):
    err = abs(math.pi - calculate_pi(i))
    if i == 1000 or i == 1700:
      print(i)
      print(err)
    output_file.write(str(i) + " " + str(err) + "\n")

  




