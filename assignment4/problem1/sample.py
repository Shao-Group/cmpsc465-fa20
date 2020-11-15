n = 0
m = 0
s = 0
INF = 1<<31

edgelist = []

def Add(x,y,v):
	global edgelist
	edgelist[y].append((x, v))


def read():	
	global n, m, s
	global h

	l = input().strip().split(' ')
	n = int(l[0])
	m = int(l[1])
	s = int(l[2])

	for i in range(n+1):
		edgelist.append([])

	for i in range(m):
		l = input().strip().split(' ')
		Add(int(l[0]), int(l[1]), int(l[2]))



read()
#Bellman-Ford

d = []
for i in range(n+1):
	d.append(INF)

d[s] = 0

#Update distance for n-1 times
for i in range(n-1):
	for j in range(1,n+1):
		for k in edgelist[j]:
			if(d[j] > d[k[0]] + k[1]):
				d[j] = d[k[0]] + k[1]

d1 = [x for x in d]

#Update distance for n-th iteration
for j in range(1,n+1):
	for k in edgelist[j]:
		if(d[j] > d[k[0]] + k[1]):
			d[j] = d[k[0]] + k[1]

for j in range(1,n+1):
	if(d1[j] != d[j]):
		print("True", end='')
		exit()
print("False", end='')