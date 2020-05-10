def f(x):
  return (x**4)/500 - (x**2)/200 - 3/250

def g(x):
  return -(x**3)/30 + x/20 +1/6

h_total = 0
x = 10
w = 0.25

while x > 2 + w:
  y_top = f(x - w)
  y_bottom = g(x - w)
  h = y_top - y_bottom
  h_total += int(h)
  x -= w

print(h_total)

