def f(x):
  return (x**4)/500 - (x**2)/200 - 3/250

def g(x):
  return -(x**3)/30 + x/20 +1/6

p_left = 0

x_per_iteration = 0.0000005
x = 2 + x_per_iteration


while x <= 10:
  y_top = f(x)
  y_bottom = g(x)
  y = y_top - y_bottom
  p = y * x_per_iteration
  p_left += p
  x += x_per_iteration

print(p_left)
