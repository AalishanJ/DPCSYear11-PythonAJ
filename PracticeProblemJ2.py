n = input("")
n = int(n)
a = input("")
b = input("")
ctr = 0

for i in range(n):
	if (a[i:i+1] == "C" and b[i:i+1] == "C"):
		ctr = ctr + 1
	else:
		ctr = ctr

print(ctr)