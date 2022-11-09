import math


while True:
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    print(math.degrees(math.atan2(y1-y0,x1-x0)))