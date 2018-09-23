
def findSum(num):
	s = 0 
	while num > 0 :
		x = num % 10
		num = num//10
		s = s + x
	
	return s


def checkHarshad(n):
		if (n % findSum(n) == 0):
			return True
		return False

low = input()
low = int(low)
high = input()
high = int(high)

for i in range(low,high,1):
	print (checkHarshad(i))

