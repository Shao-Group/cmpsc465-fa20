seq = input().strip()
n = len(seq)

#Initialize dp table f
# f[i][j] representing the length of the longest palindromic subsequence of sequence[i,j]

f = []
for i in range(n):
	tmp = [0] * n
	f.append(tmp)

#Base cases

for i in range(n):
	f[i][i] = 1
	if(i < n-1):
		if seq[i] == seq[i+1]:
			f[i][i+1] = 2
		else:
			f[i][i+1] = 1

ans = 1

for i in range(2, n):
	for j in range(n):
		k = j + i
		if(k >= n):
			break

		f[j][k] = max(f[j+1][k], f[j][k-1])

		if(seq[j] == seq[k]):
			f[j][k] = max(f[j+1][k-1] + 2, f[j][k])

		if(f[j][k] > ans): #Update answer
			ans = f[j][k]

print(ans, end= '')


