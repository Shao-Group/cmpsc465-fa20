def getArray():	
	line = input()

	line = line.strip().split(' ')[1:]

	s = []
	for x in line:
		s.append(int(x))

	return s

def merge(s1, s2):
	n1 = len(s1)
	n2 = len(s2)
	p1 = 0
	p2 = 0

	s = []
	while(p1 < n1 or p2 < n2):
		if(p1 < n1 and (p2 >= n2 or s1[p1] < s2[p2])):
			s.append(s1[p1])
			p1 += 1
		else:
			s.append(s2[p2])
			p2 += 1

	return s


def output(s):
	print (len(s), end = ' ')
	print (' '.join(map(str, s)), end = '')
	
s1 = getArray()
s2 = getArray()
s = merge(s1, s2)
output(s)
