import Point
import Utils

A = Point.Point('A', 0, 0, 1) 
B = Point.Point('B', 4, 0, 0)
C = Point.Point('C', 2, 3, 0)

print(Utils.Utils.getNormalVector(A, B, C))