def getArray():	
	line = input()
	line = input()

	line = line.strip().split(' ')

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



def merge_sort(s):

	if(len(s) == 1):
		return s

	n = int(len(s)/2)

	s1 = merge_sort(s[:n])
	s2 = merge_sort(s[n:])
	s_merge = merge(s1, s2)

	return s_merge

def output(s):
	print (' '.join(map(str,s)))

s = getArray()
s = merge_sort(s)
output(s)