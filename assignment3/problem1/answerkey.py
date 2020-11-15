n = 0
m = 0

#Edge List
edgelist = []

#Reverse Edge List
edgelistr = []

#Build Graph
def Add(x,y):
	global edgelist
	edgelist[x].append(y)

#Build Reverse Graph
def AddR(x,y):
	global edgelist
	edgelistr[x].append(y)

def read():	
	global n, m
	global h, hr

	l = input().strip().split(' ')
	n = int(l[0])
	m = int(l[1])

	for i in range(n+1):
		edgelist.append([])
		edgelistr.append([])


	for i in range(m):
		l = input().strip().split(' ')
		Add(int(l[0]), int(l[1]))
		AddR(int(l[1]), int(l[0]))



visited = []
post = []

#dfs Reverse Graph
def dfsr(x):
	visited[x] = 1

	for i in edgelistr[x]:
		if(visited[i] == 0):
			dfsr(i)

	global post
	post.append(x)


#dfs Graph
def dfs(x):
	visited[x] = 1


	for i in edgelist[x]:
		if(visited[i] == 0):
			dfs(i)


read()
for i in range(n+1):
	visited.append(0)

for i in range(1,n+1):
	if(visited[i] == 0):
		dfsr(i)

post.reverse()

ans = 0
for i in range(n+1):
	visited[i] = 0

for i in post:
	if(visited[i] == 0):
		dfs(i)
		ans += 1

print(ans, end = '')
