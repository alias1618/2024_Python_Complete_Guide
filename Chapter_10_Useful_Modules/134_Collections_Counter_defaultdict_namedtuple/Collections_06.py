from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', ['x', 'y'])

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(line_length)
