def getArray():	
	line = input()
	n = int(line)


	lines = []
	for i in range(n):
		line = input().strip().split(' ')
		line = [float(line[0]), float(line[1])]
		lines.append(line)
	return lines

#Convert input lines into points in dual plane
def dual(lines):
	points = []
	for line in lines:
		points.append([line[0], -line[1]])
	return points

ori = [0,0]

#Convert a cmp= function into a key= function
def cmp_to_key(mycmp):
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

#Sort points in increasing order of angel wrt p*
def compare(a,b):
	global ori

	x0 = a[0] - ori[0]
	y0 = a[1] - ori[1]
	x1 = b[0] - ori[0]
	y1 = b[1] - ori[1]

	return x0 * y1 - x1 * y0

def sortPoints(points):
	chosen = 0
	for i in range(1, len(points)):
		if(points[i][1] < points[chosen][1]):
			chosen = i

	global ori 
	ori = points[chosen]
	points.pop(chosen)
	points = sorted(points, key = cmp_to_key(compare), reverse=True)
	points.insert(0, ori)

	return points

# Graham Scan Algorithm

def grahamScan(points):
	s = []
	s.append(points[0])
	s.append(points[1])
	s.append(points[2])

	for i in range(3, len(points)):
		while(len(s) >= 2):
			x0 = s[-1][0] - s[-2][0]
			y0 = s[-1][1] - s[-2][1]
			x1 = points[i][0] - s[-2][0]
			y1 = points[i][1] - s[-2][1]
			if(x0 * y1 > x1 * y0):
				break

			s.pop(-1)

		s.append(points[i])

	return s	

lines = getArray()
points = dual(lines)
points = sortPoints(points)
points = grahamScan(points)

x_max = -1e10
x_min = 1e10
maxpos = 0
minpos = 0

#Find the leftest point and rightest point

for p in range(len(points)):
	if(points[p][0] > x_max):
		x_max = points[p][0] 
		maxpos = p
	if(points[p][0] < x_min):
		x_min = points[p][0] 
		minpos = p

if(minpos > maxpos):
	upper = maxpos + 1 + len(points) - minpos
	lower = minpos - maxpos + 1
else:
	lower = minpos + 1 + len(points) - maxpos
	upper = maxpos - minpos + 1

print(upper, lower, end='')
