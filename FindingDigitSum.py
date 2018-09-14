
def findSum(num):
	s = 0 
	while num > 0 :
		x = num % 10
		num = num//10
		s = s + x
		print s

findSum(720)
