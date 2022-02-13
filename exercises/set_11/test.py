import math
from geometry_2D import Point, Circle, Polygon
from visualiser import Visualiser

vis = Visualiser()

# add a circle at 0,0 with radius 1
vis.add(Circle(Point(0,0),1))

# add some regular polygons inscribed in the previous circle
for sides in range(3,7):
  a = math.radians(360 / sides)
  poly = Polygon([ Point( math.cos(a * i), math.sin(a * i) )
                   for i in range(sides) ])
  vis.add(poly)

vis.wait_close()
