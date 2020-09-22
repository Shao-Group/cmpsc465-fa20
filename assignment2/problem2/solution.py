import matplotlib.pyplot as plt

def cross(o, a, b):
    """
    Calculates cross between two vectors.

    :param o, a: vector
    :param o, b: vector
    :return: cross product
    """
    ox, oy = o
    ax, ay = a
    bx, by = b

    return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)

def convex(points):
    """
    Calculates the concave hull for a list of points. Each point is a tuple
    containing the x- and y-coordinate.

    :param points: list of points
    :return: convex hull
    """
    dataset = sorted(set(points))  # Remove duplicates
    if len(dataset) <= 1:
        return dataset

    # Build lower hull
    lower = []
    for p in dataset:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(dataset):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    #return lower[:-1] + upper[:-1]
    return lower,upper
#points=[(-3.4,-2.15),(3.74,-7.94),(-1.94,-1.82),(0.82,2.16),(0.43,-9.54),(0.62,7.27),(1.06,-6.12),(-4.99,3.86),(-0.22,0.66),(-3.55,6.51)]
#points=[(-3.4,2.15),(3.74,7.94),(-1.94,1.82),(0.82,-2.16),(0.43,9.54),(0.62,-7.27),(1.06,6.12),(-4.99,-3.86),(-0.22,-0.66),(-3.55,-6.51)]

#points=[(-3,-10),(-1,-8),(-0.5,1),(0.5,-1),(0.5,2),(0,5),(1,5)]
#concave = hull.concave(points, 3)

print('Please input line number:')
n = int(input())
print('Please input a b of line:')
data = []
for i in range(n):
    line = input().split()
    data.append(line)
points=[]
for i in range(n):
    points.append((float(data[i][0]),float(data[i][1])))
lower,upper = convex(points)
print(len(upper),len(lower))

