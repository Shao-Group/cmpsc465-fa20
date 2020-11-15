n = 0
m = 0
s = 0
INF = 1<<31

edgelist = []

def Add(x,y,v):
	global edgelist
	edgelist[x].append((y, v))

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

d = [] # Distance
heap = [] # Binaray heap
pos = [] # The position in heap

def delete_min():
	global heap,d,pos

	k = len(heap) - 1
	heap[0] = heap[k]
	pos[heap[k]] = 0
	
	heap.pop()
	k -= 1
	x = 0

	while(x * 2 + 1 <= k):
		if(d[heap[x]] < d[heap[x *2 + 1]] and (x * 2 + 1 == k or d[heap[x]] < d[heap[x * 2 + 2]])):
			break

		if(x * 2 + 1 == k or d[heap[x * 2 + 1]] < d[heap[x * 2 + 2]]):
			heap[x], heap[x * 2 + 1] = heap[x * 2 + 1], heap[x] # Swap the value

			pos[heap[x]] = x # Update the position
			pos[heap[x * 2 + 1]] = x * 2 + 1

			x = x * 2 + 1

		else:
			heap[x], heap[x * 2 + 2] = heap[x * 2 + 2], heap[x] # Swap the value

			pos[heap[x]] = x # Update the position
			pos[heap[x * 2 + 2]] = x * 2 + 2

			x = x * 2 + 2


def bubble_up(x):
	global heap, d, pos

	while(x > 0):
		y = (x-1)//2
		if(d[heap[x]] > d[heap[y]]):
			break

		heap[x], heap[y] = heap[y], heap[x] # Swap the value

		pos[heap[x]] = x # Update the position
		pos[heap[y]] = y

		x = y


read()

#Initialization
for i in range(n+1):
	pos.append(-1)
	d.append(INF)


d[s] = 0
pos[s] = 0

#Dijkstra algorthm

heap.append(s)
for i in range(1, n+1):
	if(i != s):
		heap.append(i)
		pos[i] = len(heap) - 1 #Record the position in heap

for i in range(n):
	x = heap[0]
	delete_min()

	for e in edgelist[x]:

		if(d[e[0]] > d[x] + e[1]):
			d[e[0]] = d[x] + e[1]
			bubble_up(pos[e[0]])

#Output

for i in range(1,n):
	if(d[i] == INF):
		print(-1)
	else:
		print(d[i])


if(d[n] == INF):
	print(-1, end = '')
else:
	print(d[n], end = '')